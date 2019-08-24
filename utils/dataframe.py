import pandas as pd
def list_issues():
    
    global dfo
    global df
    global desc
    global desc1
    global start_date
    global end_date
    global start_date1
    global end_date1
    global u
    global x1
    global y1
    global x2
    global y2
    global x3
    global y3
    global x4
    global y4
    global x5
    global y5
    global x6
    global y6
    global c
    global y
    global z
    global q
    global da
    global zassi
    global ye
    global suma
    global zup
    
    global suma1
    global r1
    global s1
    global r2
    global s2
    global s22
    global r3
    global s3
    global r4
    global s4
    global r5
    global s5
    global r6
    global s6
    global ya
    global d1
    global z1
    global q1
    global zup1
    
############################################################
    u=''
    start_date=''
    end_date=''
    start_date1=''
    end_date1=''
    dfo = pd.read_excel('static/df/Stories_Report(overall_project).xlsx')
    del dfo['Unnamed: 0']
    dfo.index += 1
    desc1 = dfo.describe(include='all')

    r1 = dfo['Key'].dropna().unique()
    dfo["Story_Points"].replace([None], 0, inplace=True)
    s1 = dfo['Story_Points'].tolist()

    r2 = dfo['Assignee'].dropna().unique()
    gk = dfo.groupby('Assignee')
    s2 = [None] * len(r2)
    i = 0
    suma1=0
    for assignee in r2:
        s2[i] = gk.get_group(assignee)['Story_Points'].sum()
        suma1=suma1+s2[i]
        i = i + 1

    s22 = [None] * len(r2)
    i = 0;
    for assignee in r2:
        s22[i] = gk.get_group(assignee)['Key'].count()
        i = i + 1
    
    r3 = dfo['Status'].dropna().unique()
    sk = dfo.groupby('Status')
    s3 = [None] * len(r3)
    i = 0;
    for status in r3:
        s3[i] = sk.get_group(status)['Key'].count()
        i = i + 1
   
    z = []
    for status in r3:
        d = [None] * (len(r2) + 1)
        d[0] = status
        j = 1
        for assignee in r2:
            y = gk.get_group(assignee)
            n = y['Status'].dropna().unique()
            if (status in n):
                d[j] = len(y[y['Status'] == status])
            else:
                d[j] = 0
            j = j + 1
        z.append(d)
        i = i + 1
    z1 = z

    zup1=[]
    status = 'Done'
    d = [None] * ( len(r2) +1)
    f = [None] * (len(r2) + 1 )
    d[0]= "Sum of story-points"
    f[0]= "No. of stories"
    j = 1
    for assignee in r2:
        y = gk.get_group(assignee)
        n = y['Status'].dropna().unique()
        if (status in n):
            d[j] = y[y['Status'] == status]['Story_Points'].sum()
            f[j] = len(y[y['Status'] == status])
        else:
            d[j] = 0
            f[j] = 0
        j = j + 1
    zup1.append(f)
    zup1.append(d)
    
    r4 = dfo['Releases'].dropna().unique()
    sk = dfo.groupby('Releases')
    s4 = [None] * len(r4)
    i = 0;
    for relea in r4:
        s4[i] = sk.get_group(relea)['Key'].count()
        i = i + 1

    z = []
    for status in r3:
        d = [None] * (len(r4) + 1)
        d[0] = status
        j = 1
        for rele in r4:
            y = sk.get_group(rele)
            n = y['Status'].dropna().unique()
            if (status in n):
                d[j] = len(y[y['Status'] == status])
            else:
                d[j] = 0
            j = j + 1
        z.append(d)
        i = i + 1
    ya = z
    
    r5 = dfo['Epic_Link'].dropna().unique()
    nk = dfo.groupby('Epic_Link')
    s5 = [None] * len(r5)
    i = 0;
    for epic in r5:
        s5[i] = nk.get_group(epic)['Key'].count()
        i = i + 1

    z = []
    for status in r3:
        d = [None] * (len(r5) + 1)
        d[0] = status
        j = 1
        for epic in r5:
            y = nk.get_group(epic)
            n = y['Status'].dropna().unique()
            if (status in n):
                d[j] = len(y[y['Status'] == status])
            else:
                d[j] = 0
            j = j + 1
        z.append(d)
        i = i + 1
    q1 = z
   
    r6 = dfo['Story_Points'].dropna().unique()  
    spk = dfo.groupby('Story_Points')
    s6 = [None] * len(r6)
    i = 0;
    for sp in r6:
        s6[i] = spk.get_group(sp)['Key'].count()
        i = i + 1
    #############################################################################################33
    df = pd.read_excel('static/df/Stories_Report(selected_time_period).xlsx')
    del df['Unnamed: 0']
    df.index += 1
    desc = df.describe(include='all')

    x1 = df['Key'].dropna()
    x1 = x1.unique()
    df["Story_Points"].replace([None], 0, inplace=True)
    y1 = df['Story_Points'].tolist()

    x2 = df['Assignee'].dropna().unique()
    gk = df.groupby('Assignee')
    y2 = [None] * len(x2)
    i = 0
    suma=0
    for assignee in x2:
        y2[i] = gk.get_group(assignee)['Story_Points'].sum()
        suma=suma + y2[i]
        i = i + 1

    c = [None] * len(x2)
    i = 0;
    for assignee in x2:
        c[i] = gk.get_group(assignee)['Key'].count()
        i = i + 1

    x3 = df['Status'].dropna().unique()
    sk = df.groupby('Status')
    y3 = [None] * len(x3)
    i = 0;
    for status in x3:
        y3[i] = sk.get_group(status)['Key'].count()
        i = i + 1

    z = []
    for status in x3:
        d = [None] * (len(x2) + 1)
        d[0] = status
        j = 1
        for assignee in x2:
            y = gk.get_group(assignee)
            n = y['Status'].dropna().unique()
            if (status in n):
                d[j] = len(y[y['Status'] == status])
            else:
                d[j] = 0
            j = j + 1
        z.append(d)
        i = i + 1
    zassi = z

    zup=[]
    status = 'Done'
    d = [None] * ( len(x2) +1)
    f = [None] * (len(x2) + 1 )
    d[0]= "Sum of story-points"
    f[0]= "No. of stories"
    j = 1
    for assignee in x2:
        y = gk.get_group(assignee)
        n = y['Status'].dropna().unique()
        if (status in n):
            d[j] = y[y['Status'] == status]['Story_Points'].sum()
            f[j] = len(y[y['Status'] == status])
        else:
            d[j] = 0
            f[j] = 0
        j = j + 1
    zup.append(f)
    zup.append(d)
    
    x4 = df['Releases'].dropna().unique()
    sk = df.groupby('Releases')
    y4 = [None] * len(x4)
    i = 0;
    for relea in x4:
        y4[i] = sk.get_group(relea)['Key'].count()
        i = i + 1

    z = []
    for status in x3:
        d = [None] * (len(x4) + 1)
        d[0] = status
        j = 1
        for rele in x4:
            y = sk.get_group(rele)
            n = y['Status'].dropna().unique()
            if (status in n):
                d[j] = len(y[y['Status'] == status])
            else:
                d[j] = 0
            j = j + 1
        z.append(d)
        i = i + 1
    ye = z

    x5 = df['Epic_Link'].dropna().unique()
    nk = df.groupby('Epic_Link')
    y5 = [None] * len(x5)
    i = 0;
    for epic in x5:
        y5[i] = nk.get_group(epic)['Key'].count()
        i = i + 1

    z = []
    for status in x3:
        d = [None] * (len(x5) + 1)
        d[0] = status
        j = 1
        for epic in x5:
            y = nk.get_group(epic)
            n = y['Status'].dropna().unique()
            if (status in n):
                d[j] = len(y[y['Status'] == status])
            else:
                d[j] = 0
            j = j + 1
        z.append(d)
        i = i + 1
    global q
    q = z
    
    x6 = df['Story_Points'].dropna().unique()
    spk = df.groupby('Story_Points')
    y6 = [None] * len(x6)
    i = 0;
    for sp in x6:
        y6[i] = spk.get_group(sp)['Key'].count()
        i = i + 1