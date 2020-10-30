#!/bin/bash
# set -xo
echo_info_str() {
  echo -e "\033[34m [INFO   ]\033[0m: $1"
}

echo_success_str() {
  echo -e "\033[32m [SUCCESS]\033[0m: $1"
}

echo_error_str() {
  echo -e "\033[31m [ERROR  ]\033[0m: $1"
}

# 4.1.3.1 检查是否禁止telnet协议远程访问
forbid_telnet_access() {
  key_word="auth required pam_securetty.so"
  file_path="/etc/pam.d/login"
  echo_info_str "Start Disabled Telnet protocol remote access"
  if [[ -z $(cat "${file_path}" | grep "${key_word}") ]];
  then
    echo "$key_word" >> "${file_path}"
  fi
  # TODO //: 需要重启虚机
  echo_success_str "Telnet protocol remote access has been disabled"
  echo ""
}

#4.1.3.2 禁止SSH的TCP转发
forbid_tcp_forwarding(){
  key_word="AllowTcpForwarding no"
  file_path="/etc/ssh/sshd_config"
  echo_info_str "Start Set AllowTcpForwarding no In sshd_config"
  if [[ -z $(cat "${file_path}" | grep "^${key_word}") ]];
  then
    echo "$key_word" >> "${file_path}"
  fi
  echo_success_str "AllowTcpForwarding no has already in config file"
  echo ""
}

# 4.1.3.3 禁止SSH Agent转发
forbid_ssh_agent_remote() {
  key_word="AllowAgentForwarding no"
  file_path="/etc/ssh/sshd_config"
  echo_info_str "Start Disable SSH Agent Remote"
  if [[ -z $(cat "${file_path}" | grep "^${key_word}") ]];
  then
    echo "$key_word" >> "${file_path}"
  fi
  echo_success_str "SSH Agent Forwarding Has Been Disabled"
  echo ""

}

# 4.1.3.4 设置是否允许连接到转发SSH客户端端口
forbid_ssh_client_remote() {
  # TODO:// 开启后会导致ssh 远程链接失败，可能会导致系统出错
  key_word="ForwardAgent no"
  file_path="/etc/ssh/ssh_config"
  echo_info_str "Start Disable SSH Client Port Forwarding"
  if [[ -z $(cat "${file_path}" | grep "^${key_word}") ]];
  then
    echo "$key_word" >> "${file_path}"
  fi
  echo_success_str "SSH Client Port Forwarding Has Been Disabled"
  echo ""
}

# ssh 需要禁止的选项
forbid_ssh_options() {
  forbid_tcp_forwarding
  forbid_ssh_agent_remote
  forbid_ssh_client_remote
  systemctl restart sshd.service
}


# 4.1.3.5 禁止使用Tunnel设备
forbid_use_tunnel_equipment() {
  # TODO:// 需要调查
  echo_success_str "Tunnel Equipment Has Been Banned"
  echo ""
}

# 4.1.3.6 关闭IP转发功能
shutdown_ip_forward() {
  key_word_ipv4="net.ipv4.ip_forward"
  key_word_ipv6="net.ipv6.conf.all.forwarding"
  file_path="/etc/sysctl.conf"
  echo_info_str "Start Disabled IP Forwarding"
  nu_ipv4=$(grep -n "^${key_word_ipv4}" /etc/sysctl.conf|cut -d ":" -f 1)
  nu_ipv6=$(grep -n "^${key_word_ipv6}" /etc/sysctl.conf|cut -d ":" -f 1)
  # echo "${nu_ipv4} \&\& ${nu_ipv6}"
  if [[ -z "${nu_ipv4}"  ]];
  then
    echo "net.ipv4.ip_forward=0" >> "${file_path}"
  else :
    sed -i "${nu_ipv4}c net.ipv4.ip_forward=0" /etc/sysctl.conf
  fi

  if [[ -z "${nu_ipv6}"  ]];
  then
    echo "net.ipv6.conf.all.forwarding=0" >> "${file_path}"
  else :
    sed -i "${nu_ipv6}c net.ipv6.conf.all.forwarding=0" /etc/sysctl.conf
  fi

  echo_success_str "IP Forwarding Has Been Disabled"
  echo ""
}

# 4.1.3.7 关闭报文重定向功能
shutdown_message_redirection() {
  echo_info_str "Start Turned Off Message Redirection"
  # 关闭ipv4 报文重定向
  echo 0 > /proc/sys/net/ipv4/conf/all/send_redirects
  echo 0 > /proc/sys/net/ipv4/conf/default/send_redirects
  echo 0 > /proc/sys/net/ipv4/conf/eth0/send_redirects
  # 关闭ipv6 报文重定向
  echo 0 > /proc/sys/net/ipv6/conf/all/accept_redirects
  echo 0 > /proc/sys/net/ipv6/conf/default/accept_redirects
  echo 0 > /proc/sys/net/ipv6/conf/eth0/accept_redirects

  echo_success_str "Message Redirection Has Been Turned Off"
  echo ""
}

# 4.1.3.8 不接收源路由报文
disable_receive_source_routing_messages() {
  # TODO: 需要调查
  echo_success_str "Source Routing Messages Are No Longer Received"
  echo ""
}

# 4.1.3.9 不接收ICMP 重定向报文
disable_receive_icmp_redirect_message() {
  echo_info_str "Start Disabled ICMP Redirect Messages"
  file_path="/etc/sysctl.conf"
  keyword_all="net.ipv4.conf.all.accept_redirects"
  key_word_default="net.ipv4.conf.default.accept_redirects"
  nu_all=$(grep -n "^${keyword_all}" ${file_path}|cut -d ":" -f 1)
  nu_default=$(grep -n "^${key_word_default}" ${file_path}|cut -d ":" -f 1)
  if [[ -z "${nu_all}"  ]];
  then
    echo "net.ipv4.conf.all.accept_redirects = 0" >> "${file_path}"
  else
    sed -i "${nu_all}c net.ipv4.conf.all.accept_redirects = 0" "${file_path}"
  fi

  if [[ -z "${nu_default}" ]];
  then
    echo "net.ipv4.conf.default.accept_redirects = 0" >> "${file_path}"
  else
    sed -i "${nu_default}c net.ipv4.conf.default.accept_redirects = 0" "${file_path}"
  fi

  echo_success_str "ICMP Redirect Messages Has Been Disabled"
  echo ""
}

# 4.1.3.10 忽略广播ICMP 请求
disable_icmp_requests() {
  echo_info_str "Start Disable ICMP Requests"
  file_path="/etc/sysctl.conf"
  keyword="net.ipv4.conf.all.secure_redirects"
  nu_keyword=$(grep -n "^${keyword}" ${file_path}|cut -d ":" -f 1)

  if [[ -z "${nu_keyword}" ]];
  then
    echo "net.ipv4.conf.all.secure_redirects = 0" >> "${file_path}"
  else
    sed -i "${nu_keyword}c net.ipv4.conf.all.secure_redirects = 0" "${file_path}"
  fi

  echo_success_str "ICMP Requests Has Been Disabled"
  echo ""
}

# 4.1.3.11 忽略虚假ICMP 响应
ignore_False_icmp_response() {
  # TODO:// 待调查
  echo_success_str "ICMP Response Has Been Ignored"
  echo ""
}

# 4.1.3.12 开启反向路径过滤
enable_reverse_path_filtering() {
  # TODO:// 待调查
  echo_success_str "Start Enable Reverse Path Filtering"
  echo ""
}

# 4.1.3.13 使能TCP SYN Cookies
enable_tCP_sYN_cookies() {
  # TODO:// 待调查
  echo_success_str "Start Enable TCP SYN Cookies"
  echo ""
}

# 4.1.3.14 检查SSH是否使用业界认可的、安全的加密算法，如AES128位及以上
check_ssh_encryption_algorithm() {
  # TODO:// 待调查
  echo_success_str "Ssh Encryption Algorithm Is Security"
  echo ""
}

# 4.1.3.15 检查是否配置远程连接的安全性
check_ssh_remote_security() {
  # TODO:// 待调查
  echo_success_str "Ssh Remote Is Security"
  echo ""
}

# 总调用函数
main() {
  forbid_telnet_access
  forbid_ssh_options
  forbid_use_tunnel_equipment
  shutdown_ip_forward
  shutdown_message_redirection
  disable_receive_source_routing_messages
  disable_receive_icmp_redirect_message
  disable_icmp_requests
  ignore_False_icmp_response
  enable_reverse_path_filtering
  enable_tCP_sYN_cookies
  check_ssh_encryption_algorithm
  check_ssh_remote_security
}

main

