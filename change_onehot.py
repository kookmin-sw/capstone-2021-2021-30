def change_onehot(labels):
  one_hot = [[] for _ in range(21)]

  i = 0
  for each in one_hot: #-10 ~ 10
    for k in range(21):
      each.append(0)
    each[i] = 1
    i+=1

  for i in range(len(labels)):
    if(labels[i] == -10): labels[i] = one_hot[0]
    if(labels[i] == -9): labels[i] = one_hot[1]
    if(labels[i] == -8): labels[i] = one_hot[2]
    if(labels[i] == -7): labels[i] = one_hot[3]
    if(labels[i] == -6): labels[i] = one_hot[4]
    if(labels[i] == -5): labels[i] = one_hot[5]
    if(labels[i] == -4): labels[i] = one_hot[6]
    if(labels[i] == -3): labels[i] = one_hot[7]
    if(labels[i] == -2): labels[i] = one_hot[8]
    if(labels[i] == -1): labels[i] = one_hot[9]
    if(labels[i] == 0): labels[i] = one_hot[10]
    if(labels[i] == 1): labels[i] = one_hot[11]
    if(labels[i] == 2): labels[i] = one_hot[12]
    if(labels[i] == 3): labels[i] = one_hot[13]
    if(labels[i] == 4): labels[i] = one_hot[14]
    if(labels[i] == 5): labels[i] = one_hot[15]
    if(labels[i] == 6): labels[i] = one_hot[16]
    if(labels[i] == 7): labels[i] = one_hot[17]
    if(labels[i] == 8): labels[i] = one_hot[18]
    if(labels[i] == 9): labels[i] = one_hot[19]
    if(labels[i] == 10): labels[i] = one_hot[20]
    if(labels[i] == 11): labels[i] = one_hot[20]

  return labels
