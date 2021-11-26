import requests
import sys
import time
from xml.etree import ElementTree


QUERY_URL = 'http://nl.go.kr/kolisnet/openApi/open.php'


def search_book(keyword="황순원"):
    """[summary]
    
    Keyword Arguments:
        keyword {str} -- keyword for book search (default: {"황순원"})
    
    Returns:
        {str} -- search result in plain txt.
    """

    query = { "page":str(1), 
              "per_page":str(1000), 
              "collection_set":1,
              "sort_ksj":"SORT_TITLE ASC",
              "search_field1":"total_field", 
              "value1":keyword }
    r = requests.get(QUERY_URL, params=query)
    #print(r)
    #print(r.text)
    tree = ElementTree.fromstring(r.content)
    print(xml_tree_stringfy(tree))
    return xml_tree_stringfy(tree)
    

def search_seoul_libs():
    """
        도서관정보 조회
        http://nl.go.kr/kolisnet/openApi/open.php?lib_code=011006

        소장도서관 지역 정보
        11(서울),21(부산),22(대구),23(인천),
        24(광주),25(대전),26(부산광역시),
        27(대구광역시),28(인천광역시),
        29(광주광역시),30(대전광역시),
        31(울산),41(경기),42(강원),43(충북),
        44(충남),45(전북),46(전남),47(경북),
        48(경남),49(제주)
    """
    
    query = { "lib_code":"111001" }

    for i in range(1, 1000):
        query["lib_code"] = "111%03d"%i
        r = requests.get(QUERY_URL, params=query)
        print("------ `%s` "%query["lib_code"])
        print(r)
        print(r.text)
        time.sleep(2)


def print_xml_tree(node, indent="  "):
    """print xml tree structure recursively
    
    Arguments:
        node {} -- xml node
    
    Keyword Arguments:
        indent {str} -- indent for tree depth (default: {"  "})
    """

    text = node.text.strip() if node.text else ''
    print(indent, node.tag, ':', text)
    for c in node:
        print_xml_tree(c, indent+"  ")
    return


def xml_tree_stringfy(node, indent="  "):
    """make a string of xml tree structure recursively
    
    Arguments:
        node {[type]} -- xml node
    
    Keyword Arguments:
        indent {str} -- indent for tree depth (default: {"  "})
    """

    text = node.text.strip() if node.text else ''
    s = indent + node.tag + ' : ' + text + '\n'
    for c in node:
        s += xml_tree_stringfy(c, indent+"  ")
    return s


if __name__ == '__main__':
    if len(sys.argv) > 1:
        keyword = sys.argv[1]
        search_book(keyword)
    else:
        search_book()