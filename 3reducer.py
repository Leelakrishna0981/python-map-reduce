s = open("02.txt","r")
r = open("03.txt", "w")

count = 0
thiskey = ""
thisvalue = 0


for line in s:
  data = line.strip()
  paymentType= data

  if thiskey == "":
    if paymentType:
      thiskey = paymentType

  # apply the aggregation function
  
  if paymentType == thiskey:
    #thisvalue = thisvalue + float(amount)
    count = count + 1
  else:
    r.write( thiskey + '\t' + str(count)+'\n')
    # start over when changing keys
    thiskey = paymentType
   # thisvalue = float(amount)
    count = 1

  # output final entry

r.write( thiskey + '\t' + str(count)+'\n')

s.close()
r.close()