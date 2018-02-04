## VB

```vb
'== Basic
dim x: x = 1
dim arr: arr = Array(1,2,3,4)
dim arrEmpty: arrEmpty = Array()
dim dict: set dict = Server.CreateObject("Scripting.Dictionary")
dict.Add "re","Red"
dict.Add "gr","Green"
dict.Add "bl","Blue"
dict.Add "pi","Pink"
dict.count  ' count of key value pair
dict.items  ' an array of all values
dict.keys   ' an array of all keys


response.write "test value is equal to " & x

for each ele in arr
    response.write(ele)
loop

For i = 0 To Ubound(arr)
  response.write("The number is " & arr(i) & "<br />")
Next

if Ubound(arr) > 0 then
    response.write(Ubound(arr))
end if

dim sql: sql = "select * from TABLE"
dim rs: set rs = getRS(sql)
if not rs.eof and not rs.bof then
    while not rs.eof
        response.write(rs("ID"))
        rs.movenext
    Wend
end if


' switch, no need to use break;
Select Case x
    Case 1 then response.write("x equal 1")
    Case 2 then response.write("x equal 2")
end select

'== function/sub
function foo()
    foo=1
end function

sub subfoo()
    response.write("test sub")
end sub

'== request
request.querystring("id")
request.form("id")
request("id")

Session.Timeout=5
Session.Abandon
```

## C++

```c++
int i = 1;

```

## C#

```c#
int i = 1;
String str = "test str"
List<String> strList = new List<String>();
strList.Add("test 1");
strList.Add("test 2");
List<int> intList = new List<int>(new int[]{1,2,3});

class cube{
    private double length{get;set;}
    private double height{get;set;}
    private double width{get;set;}
    
    public double getVolume(){
        return length*height*width;
    }
};

foreach (int i in intList){
    Console.WriteLine(i);
}

for(int i=0; i<intList.Count; i++){
    Console.WriteLine(i);
}

```

## Python

```python

```
