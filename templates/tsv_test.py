import csv
import os
import re
folder_lyc = 'lyc'
folder_syc  = 'syc'
folder_inf  = 'inf'
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

    def fix_file_name(file_name):
        new_file_name = re.sub('[\/:*?"<>|]','',file_name)
        if len(new_file_name) > 10:
            new_file_name = new_file_name[:10]
        return new_file_name

    if __name__ == '__main__':
        file_name = 'sync_lyric_listen_20210224.tsv'
        f = open(file_name, 'r', encoding='utf-8')
        rdr = csv.reader(f, delimiter='\t')
        r = list(rdr)
        createFolder(folder_lyc)
        createFolder(folder_syc)
        createFolder(folder_inf)
        print('len'+ str(len(r)))
        for i in range(0, len(r)-1):
            index = i + 1
            artist = fix_file_name(r[index ][1])
            title  = fix_file_name(r[index ][2])
            inf_file_name = os.path.join(folder_inf, str(i)+'_'+artist+'_'+title+'.txt')
            lyc_file_name = os.path.join(folder_lyc, str(i)+'.txt')
            syc_file_name = os.path.join(folder_syc, str(i)+'.txt')
            i_f = open(inf_file_name, 'wt', encoding='utf-8')
            l_f = open(lyc_file_name, 'wt', encoding='utf-8')
            s_f = open(syc_file_name, 'wt', encoding='utf-8')
            i_f.write(r[index][0]+'\t'+r[index ][1]+'\t'+r[index ][2]+'\t'+r[index ][3]+'\t'+r[index ][4]+'\t'+r[index ][5]+'\t'+r[i][6]+'\n')
            i_f.close()
            l_f.write(r[index ][8])
            l_f.close()
            s_f.write(r[index ][9])
            s_f.close()
        f.close()