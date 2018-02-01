def to_f(cel): # Convert fahrenheit to celsius
    return (cel * 9/5)+32

def wc(c,f):
    wc_list = []
    wc_list.append(c)
    wc_list.append(f)
    for val in range (5,41,5):
        if (f <= 50):
            windchill = 35.74 + (0.6215*f) - 35.75*(val**0.16) + 0.4275*f*(val**0.16)
            windchill = round(windchill, 2)
        else:
            windchill = "x"
        wc_list.append(windchill)
    return(wc_list)

def heat(c,f):
    heat_list = []
    heat_list.append(c)
    heat_list.append(f)
    for val in range (40,101,10):
        if (f >= 80):
            heatindex = -42.379 + 2.04901523*f + 10.14333127*val + -0.22475541*f*val + -6.83783*10**-3 *f**2 + -5.481717*10**-2 * val**2 + 1.22874*10**-3 * f**2 * val + 8.5282*10**-4 * f * val**2 + -1.99*10**-6 * f**2 * val**2
            heatindex = round(heatindex, 2)
        else:
            heatindex = "x"
        heat_list.append(heatindex)
    return(heat_list)
#########################

c1, c2 = input("Enter two numbers between -20 and 50: ").split()
c1 = int(c1)
c2 = int(c2)
if c1 < -20 or c2 > 50:
    print("Number Invalid")
else:

#heading
    print("Wind chill temperatures")
    print('\n')
    column=["Cel", "Fah"]
    for i in range (5, 45, 5):
        column.append(i)
    for x in column:
        print(x,end='\t')

    print('\n')
    flist = []
    for Celsisu in range (c1, c2 + 1):
        f = to_f(Celsisu)
        list1 = []
        list1 = (wc(Celsisu,f))
        for i in list1:
            print(i, end="\t")
        print()
    print('\n')
    ####################################################################
    print("Heat Index Temp")
    column_heat=["Cel", "Fah"]


    for i in range (5, 45, 5):
        column_heat.append(str(i) + "%")
    for x in column_heat:
        print(x,end='\t')

    print('\n')

    flist = []
    for val in range (c1, c2 + 1):
        f = to_f(val)
        list1 = []
        list1 = (heat(val,f))
        for i in list1:
            print(i, end="\t")
        print()
