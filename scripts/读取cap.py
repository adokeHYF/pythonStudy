# coding=gbk
import dpkt
import os
#import pdb

#pdb.set_trace()
#��ȡcap�ļ�
cap_path = r"C:\Users\abeil\Desktop\cap"

for file in os.listdir(cap_path):
      print ('list:' + file)
      file_cap = open( cap_path + '\\' +file , 'rb')
      string_data = dpkt.pcap.Reader(file_cap)



      #��cap�ļ����н���
      pkts_num = 0
      pkts_len = []
      dpktEth = dpkt.ethernet

      for Pkt in string_data:
            eth = dpktEth.Ethernet(Pkt[1])
            content = eth.data.data.data
            if len(content) != 0:
                  pkts_len.append(len(content))
            #text_cap.write('****'+ content +'\n' )
            pkts_num += 1
      #print pkts_len
      print ('PKTs��%d' % pkts_num)

      file_cap.flush()
      file_cap.close()

      #argdsize
      while input('plz input 1 or 0:')!= 0 :
            dsize = 0
            start = input('plz input a int:')
            end = input('plz input a int:')
            num = end - start + 1
            pkt_lens = pkts_len[start -1 : end]
            for i in pkt_lens:
                  #print i
                  dsize = dsize + i
            argdsize = dsize/num
            print ('argdsize: %d (%d-%d)' % (argdsize, start, end))