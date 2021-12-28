import xmltodict


s = """
<METADATA>
        <LIBINFO>
                <LIB_CODE>147056</LIB_CODE>
                <DIVISION></DIVISION>
                <ZIP_CODE>791-280             </ZIP_CODE>
                <TEL>054-270-4786</TEL>
                <FAX>054-270-47</FAX>
                <ADDRESS>경북 포항시 북구 삼호로533</ADDRESS>
                <E_MAIL>bookcafe@ipohang.org</E_MAIL>
                <HOMEPAGE>http://youth.ipohang.org</HOMEPAGE>
        </LIBINFO>
</METADATA>"""


print(xmltodict.parse(s))