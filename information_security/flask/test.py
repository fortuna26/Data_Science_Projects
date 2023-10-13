#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"></ul></div>

# In[34]:


import requests

# Example loan application
application = {
        'destination_port': 80, 
        'flow_duration': 2898065, 
        'total_fwd_packets': 5,
       'total_backward_packets': 0, 
        'total_length_of_fwd_packets': 30,
       'total_length_of_bwd_packets': 0, 
        'fwd_packet_length_max': 6,
       'fwd_packet_length_min': 6, 
        'fwd_packet_length_mean': 6.0,
       'fwd_packet_length_std': 0.0, 
        'bwd_packet_length_max': 0,
       'bwd_packet_length_min': 0, 
        'bwd_packet_length_mean': 0.0,
       'bwd_packet_length_std': 0.0, 
        'flow_bytes/s': 10.351735, 
        'flow_packets/s': 1.725289,
       'flow_iat_mean': 724516.25, 
        'flow_iat_std': 1447039.1, 
        'flow_iat_max': 2895075, 
        'flow_iat_min': 982,
       'fwd_iat_total': 2898065, 
        'fwd_iat_mean': 724516.25, 
        'fwd_iat_std': 1447039.1, 
        'fwd_iat_max': 2895075,
       'fwd_iat_min': 982, 
        'bwd_iat_total': 0, 
        'bwd_iat_mean': 0.0, 
        'bwd_iat_std': 0.0,
       'bwd_iat_max': 0, 
        'bwd_iat_min': 0, 
        'fwd_psh_flags': 0, 
        'fwd_urg_flags': 0, 
        'fwd_header_length': 100,
       'bwd_header_length': 0, 
        'fwd_packets/s': 1.725289, 
        'bwd_packets/s': 0.0,
       'min_packet_length': 6, 
        'max_packet_length': 6, 
        'packet_length_mean': 6.0,
       'packet_length_std': 0.0, 
        'packet_length_variance': 0.0, 
        'fin_flag_count': 0,
       'syn_flag_count': 0, 
        'rst_flag_count': 0, 
        'psh_flag_count': 0, 
        'ack_flag_count': 1,
       'urg_flag_count': 0, 
        'cwe_flag_count': 0, 
        'ece_flag_count': 0, 
        'down/up_ratio': 0,
       'average_packet_size': 7.2, 
        'avg_fwd_segment_size': 6.0, 
        'avg_bwd_segment_size': 0.0,
       'fwd_header_length.1': 100, 
         'subflow_fwd_packets': 5, 
        'subflow_fwd_bytes': 30,
       'subflow_bwd_packets': 0, 
        'subflow_bwd_bytes': 0, 
        'init_win_bytes_forward': 256,
       'init_win_bytes_backward': -1, 
        'act_data_pkt_fwd': 4, 
        'min_seg_size_forward': 20,
       'active_mean': 0.0, 
        'active_std': 0.0, 
        'active_max': 0, 
        'active_min': 0, 
        'idle_mean': 0.0,
       'idle_std': 0.0, 
        'idle_max': 0, 
        'idle_min': 0, 
        'flow_duration_mean': 1.698616e+07
    }

# Location of my server
url = "http://192.168.1.102:8989/predict"

# Send request
resp = requests.post(url, json=application)

# Print result
print(resp.json())


# In[ ]:




