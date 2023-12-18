import xml.etree.ElementTree as ET
import pandas as pd
import csv

class Trans:
    xml_path = "test.xml"
    csv_path = "test.csv"

    """
    将xml转为csv
    """
    def xmlTrans():

        mytree = ET.parse(Trans.xml_path)
        myroot = mytree.getroot()
        print(myroot.items())

        list_ = []
        for x in myroot:
            dict01 = {}
            dict01[x.tag] = x.get("title")
            print(x.get("title"))
            for y in x:        
                dict01[y.tag] = y.text
                
            list_.append(dict01)   

        # df = pd.DataFrame(list)
        # df.to_csv('test.csv', index=False)
        # print(df)

        with open(Trans.csv_path,"w",newline='') as file:
            # 定义列名
            filesname = ["movie","type","format","year","rating","stars","description","episodes"]       
            writer = csv.DictWriter(file,fieldnames=filesname,restval='-',delimiter=',') # restval 指定当字典中缺少某个键时，该键对应的默认值。默认为空字符串
            writer.writeheader()
            writer.writerows(list)



    """
    将csv转为xml
    """
    def csvTrans():

        file = open(Trans.csv_path,"r")
        dict_data = csv.DictReader(file,dialect='excel',skipinitialspace = True)        

        root = ET.Element("collection")        
        root.attrib["shelf"] = "New Arrivals"

        for datas in dict_data:
            list01 = list(datas.keys())
            movie = ET.SubElement(root,list01[0])
            movie.attrib["title"] = datas.get(list01[0])
            for key in list01:
                if datas.get(key) != '-' and key != "movie" :
                    detl = ET.SubElement(movie,key)
                    detl.text = datas.get(key)
                else:
                    pass
        
        tree = ET.ElementTree(root)
        tree.write("test01.xml", encoding ="utf-8",xml_declaration = True)
           
        file.close()

Trans.csvTrans()



