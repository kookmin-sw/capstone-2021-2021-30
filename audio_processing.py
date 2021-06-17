#get each place value of audio that is vectorized
def audio_preprocessing(audio_datas):
  audio_datas = np.reshape(audio_datas,(1,234160))
  
  audio_datas_list =[[] for _ in range(234160)]
  
  for i in range(len(audio_datas[0])):
    if audio_datas[0][i] == 0:
      for j in range(14):
        audio_datas_list[i].append(0)
      pass
    tmp = audio_datas[0][i]*1000000000000000
    
    audio_datas_list[i].append(round(tmp/1000000000000000))
    audio_datas_list[i].append(round((tmp%1000000000000000)/100000000000000))
    audio_datas_list[i].append(round((tmp%100000000000000)/10000000000000))
    audio_datas_list[i].append(round((tmp%1000000000000)/1000000000000))
    audio_datas_list[i].append(round((tmp%1000000000000)/100000000000))
    audio_datas_list[i].append(round((tmp%100000000000)/10000000000))
    audio_datas_list[i].append(round((tmp%10000000000)/1000000000))
    audio_datas_list[i].append(round((tmp%1000000000)/100000000))
    audio_datas_list[i].append(round((tmp%100000000)/10000000))
    audio_datas_list[i].append(round((tmp%1000000)/1000000))
    audio_datas_list[i].append(round((tmp%1000000)/100000))
    audio_datas_list[i].append(round((tmp%100000)/10000))
    audio_datas_list[i].append(round((tmp%10000)/1000))
    audio_datas_list[i].append(round((tmp%1000)/100))
    audio_datas_list[i].append(round(tmp%10))
  return audio_datas_list
    
