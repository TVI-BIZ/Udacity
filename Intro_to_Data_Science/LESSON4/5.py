import csv

def fix_turnstile_data(filenames):
    '''
    Filenames is a list of MTA Subway turnstile text files. A link to an example
    MTA Subway turnstile text file can be seen at the URL below:
    http://web.mta.info/developers/data/nyct/turnstile/turnstile_110507.txt
    
    As you can see, there are numerous data points included in each row of the
    a MTA Subway turnstile text file. 

    You want to write a function that will update each row in the text
    file so there is only one entry per row. A few examples below:
    A002,R051,02-00-00,05-28-11,00:00:00,REGULAR,003178521,001100739
    A002,R051,02-00-00,05-28-11,04:00:00,REGULAR,003178541,001100746
    A002,R051,02-00-00,05-28-11,08:00:00,REGULAR,003178559,001100775
    
    Write the updates to a different text file in the format of "updated_" + filename.
    For example:
        1) if you read in a text file called "turnstile_110521.txt"
        2) you should write the updated data to "updated_turnstile_110521.txt"

    The order of the fields should be preserved. Remember to read through the 
    Instructor Notes below for more details on the task. 
    
    In addition, here is a CSV reader/writer introductory tutorial:
    http://goo.gl/HBbvyy
    
    You can see a sample of the turnstile text file that's passed into this function
    and the the corresponding updated file by downloading these files from the resources:
    
    Sample input file: turnstile_110528.txt
    Sample updated file: solution_turnstile_110528.txt
    '''
    for name in filenames:
        with open(name,'rb') as File:  
            reader = csv.reader(File,delimiter=',')
            big_list = []
            for elem in reader:
                const_l = []
                count = 0
                var_l = []
                res_l = []
                n=0
                for item in elem:
                    if count == 0:
                        for i in range(0,3):
                            const_l.append(elem[i])
                        count += 1
                        n=3
                    else:
                        if n <= len(elem):
                            for i in range(len(elem)):
                                if len(elem) > n:
                                    for z in range(0,5):
                                        var_l.append(elem[n+z])
                                    res_l = const_l + var_l  
                                    n +=5
                                    big_list.append(res_l)
                                    res_l,var_l = [],[]

        write_name = "updated_" + name
        myFile = open(write_name, 'w')
        with myFile:
            writer = csv.writer(myFile)
            writer.writerows(big_list)
    
        
        
        
        
        
        
        
        # reader = open (name, 'r')
        # write_name = 'updated_'+name
        # writer = open (write_name, 'w')
        
        # reader_in = csv.reader(reader, delimiter = ',')
        # writer_out = csv.writer(writer, delimiter =',')
        
        # for line in reader_in:

        #     line_len = len(line)

        #     c1 = line [0]
        #     c2 = line [1]
        #     c3 = line [2]

        #     i = 3
        #     while i < line_len:
        #         line_updated = [c1, c2, c3, line[i], line[i+1], line[i+2], line[i+3], line[i+4]]
        #         writer_out.writerow(line_updated)
        #         i = i +5
       
