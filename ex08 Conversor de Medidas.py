metros = int(input('Digite quantos metros deseja converter: '))
km = metros / 1000
hm = metros / 100
dam = metros / 10
dcm = metros * 10
cm = metros * 100
mm = metros * 1000
print('O valor convertido em km é {} \n '
      'O valor convertido em hm é {}\n '
      'O valor convertido em dam é {}\n,'
      'O valor convertido em dcm é {}\n,'
      ' O valor convertido em cm é {}\n'
      ' o valor convertido em mm é {}'.format(km,hm,dam,dcm,cm,mm))