from socket import SOCK_STREAM, AF_INET, socket
from flask import Flask, render_template, request
import json
import protocol

app = Flask(__name__)

n = int(input())


def value():
    f = open("C:/Users/테스터/Desktop/save.txt",'r')
    try:
        line = f.readlines()
        line = line[-1].split(',')
    except:
        line = [' ', ' ']

    return [line[0], line[1]]


@app.route('/methodd', methods=['POST'])
def methodd (num_list=[]):

    set_value=[]
    for i in range(0,n):
        value1=request.POST['grparr1']
        value2=request.POST['grparr2']
        set_value+=[value1[i],value2[i]]

    if request.method == 'POST':
        file_path = request.form['File_Path']
        url = request.form['Url']
        with open("C:/Users/테스터/Desktop/save.txt", "a", encoding='utf-8') as f:
            f.write("%s,%s\n" %(file_path, url))
            f.write('')

    get_value = value()
    for i in range(1, n + 1):
        set_value+=[file_path,url]
        if len(num_list) == n: continue
        num_list += [i]


    if set_value==[]:
        b= get_value
    else:
        b= set_value[i]

    aa = ''

    def aaa(i):
        a='''<p>
             <span class="s21">'''+str(i)+'''th</span>
             <span class="s22"> <input type="text" name="File_Path" id='File_Path' size=50 value='''+b[0]+'''></span>
             <span class="s23"> <input type="text" name="Url"  id='Url' size=50 value='''+b[1]+''' ></span>
             <span><input type="hidden" name="list1" size=50 ></span>
             <span><input type="hidden" name="list2" size=50 ></span>
             <span class="s24"> <input type="submit" value="File Open" style="width: 100px;"></span>
             <span class="s25"> <input type="submit" value="Start" style="width: 100px;"></span>
             <span class="s26"> <input type="submit" value="Stop" style="width: 100px;"></span>
             <span class="s27"> <input type="submit" value="Clear" style="width: 100px;"> </span></p></br>'''
        return a

    for i in range(1,n+1):
        aa += aaa(i)

    c='''<script type="text/javascript" src="https://code.jquery.com/jquery-3.4.0.js"></script>
         <script type="text/javascript">

        $(function(){
            $('#File_Path').on('click', function(){
		    var grpl = $("input[name=File_Path]").length;
		    var grparr1 = new Array(grpl);
		    for(var i=0; i<grpl; i++){                          
			    grparr1[i] = $("input[name=File_Path]").eq(i).val();
	        alert(grpar1r[i]);
	        }
	    });
    });
         $(function(){
            $('#Url').on('click', function(){
		    var grpl2 = $("input[name=Url]").length;
		    var grparr2 = new Array(grpl2);
		    for(var i=0; i<grpl2; i++){                          
			    grparr2[i] = $("input[name=Url]").eq(i).val();
	        alert(grparr2[i]);
	        }
	    });
    });
    </script>'''


    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    
    <meta charset="UTF-8">
    <title>VirtualCCTV</title>
  <style>


      .container1 {
        position:relative;
        top:0; right:0; left:50px;
        height: 10px;
      }

      .s11 {
         position:relative;
         left: 0x;
         border: 10px
      }

      .s12 {
         position: relative;
         left: 330px;
         border:10px
      }
     .s13 {
         position: absolute;
         left: 780px;
         border: 10px
      }
     .s14 {
         position: absolute;
         left: 890px;
         border: 10px
      }
    .s15 {
         position: absolute;
         left: 1000px;
         border: 10px
      }
    .s16 {
         position: absolute;
         left: 1110px;
         border: 10px
      }
      .container2 {
        position:absolute;
        top:50px; right:0; left:50px;
        height:10px;
      }

    .s21 {
         position:absolute;
         left: 5px;
         border:0px
         float:left;
      }

    .s22 {
         position:absolute;
         left: 50px;
         border: 10px

      }

    .s23 {
     position: absolute;
         left: 445px;
         border: 10px
      }
    .s24 {
         position:absolute;
         left: 1060px;
         border: 10px

      }
    .s25 {
         position:absolute;
         left: 1170px;
         border: 10px

      }
    .s26 {
         position:absolute;
         left: 1280px;
         border: 10px

      }
    .s27 {
         position:absolute;
         left: 1390px;
         border: 10px

      }

     .s28 {
         position:absolute;
         left: 670px;
         border: 10px

      }

    </style>
</head>

<body bgcolor="#f1f1f0">
<div>
    <form action="/methodd" method="post">
    <div class="container1">
        <span class="s11"> File Path </span>
        <span class="s12"> Url:Streaming address+port </span>
        <span class="s13"><input type="submit" value="All Start" style="width: 100px;"></span>
        <span class="s14"><input type="submit" value="All Stop"  style="width: 100px;"></span>
        <span class="s15"><input type="submit" value="All Equal" style="width: 100px;"></span>
        <span class="s16"><input type="submit" value="All Clear" style="width: 100px;"></span>
        <span class="s28"> <input type="submit" value="정보 넘기기"></span>
    </div>
    </br>

    <ul>
    ''' + aa + c +'''
</form>
</div>



</body>
</html>
'''


@app.route('/')
def test():
    get_value = value()

    num_list = []
    aa=''

    def aaa(i):
        a='''<p>
             <span class="s21">'''+str(i)+'''th</span>
             <span class="s22"> <input type="text" name="File_Path" size=50 value='''+get_value[0]+'''></span>
             <span class="s23"> <input type="text" name="Url" size=50 value='''+get_value[1]+''' ></span>
             <span><input type="hidden" name="list1" size=50 ></span>
             <span><input type="hidden" name="list2" size=50 ></span>
             <span class="s24"> <input type="submit" value="File Open" style="width: 100px;"></span>
             <span class="s25"> <input type="submit" value="Start" style="width: 100px;"></span>
             <span class="s26"> <input type="submit" value="Stop" style="width: 100px;"></span>
             <span class="s27"> <input type="submit" value="Clear" style="width: 100px;"> </span></p></br>'''
        return a


    for i in range(1, n+1):
        if len(num_list) == n: continue
        num_list += [i]
        aa += aaa(i)


    c='''<script type="text/javascript" src="https://code.jquery.com/jquery-3.4.0.js"> </script>
         <script type="text/javascript">

        $(function(){
            $('#정보 넘기기').on('click', function(){
		        var grpl = $("input[name=File_Path]").length;
		        var grparr1 = new Array(grpl);
		        for(var i=0; i<grpl; i++){                          
			        grparr1[i] = $("input[name=File_Path]").eq(i).val();
	            }
	        });
        });
        </script>
        
        <script type="text/javascript">
         $(function(){
            $('#정보 넘기기').on('click', function(){
		        var grpl2 = $("input[name=Url]").length;
		        var grparr2 = new Array(grpl2);
		        for(var i=0; i<grpl2; i++){                          
			        grparr2[i] = $("input[name=Url]").eq(i).val();
	            }
	        });
        });
    </script>'''

    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>VirtualCCTV</title>
  <style>


      .container1 {
        position:relative;
        top:0; right:0; left:50px;
        height: 10px;
      }

      .s11 {
         position:relative;
         left: 0x;
         border: 10px
      }

      .s12 {
         position: relative;
         left: 330px;
         border:10px
      }
     .s13 {
         position: absolute;
         left: 780px;
         border: 10px
      }
     .s14 {
         position: absolute;
         left: 890px;
         border: 10px
      }
    .s15 {
         position: absolute;
         left: 1000px;
         border: 10px
      }
    .s16 {
         position: absolute;
         left: 1110px;
         border: 10px
      }
      .container2 {
        position:absolute;
        top:50px; right:0; left:50px;
        height:10px;
      }

    .s21 {
         position:absolute;
         left: 5px;
         border:0px
         float:left;
      }

    .s22 {
         position:absolute;
         left: 50px;
         border: 10px

      }

    .s23 {
     position: absolute;
         left: 445px;
         border: 10px
      }
    .s24 {
         position:absolute;
         left: 1060px;
         border: 10px

      }
    .s25 {
         position:absolute;
         left: 1170px;
         border: 10px

      }
    .s26 {
         position:absolute;
         left: 1280px;
         border: 10px

      }
    .s27 {
         position:absolute;
         left: 1390px;
         border: 10px

      }

     .s28 {
         position:absolute;
         left: 670px;
         border: 10px

      }

    </style>
</head>

<body bgcolor="#f1f1f0">
<div>
    <form action="/methodd" method="post">
    <div class="container1">
        <span class="s11"> File Path </span>
        <span class="s12"> Url:Streaming address+port </span>
        <span class="s13"><input type="submit" value="All Start" style="width: 100px;"></span>
        <span class="s14"><input type="submit" value="All Stop"  style="width: 100px;"></span>
        <span class="s15"><input type="submit" value="All Equal" style="width: 100px;"></span>
        <span class="s16"><input type="submit" value="All Clear" style="width: 100px;"></span>
        <span class="s28"> <input type="submit" value="정보 넘기기"></span>
    </div>
    </br>

    <ul>
    ''' + aa + c +'''
</form>
</div>



</body>
</html>
'''




# @app.route('/socket', methods=['POST'])
# def cal():
#
#     if request.method == 'POST':
#         file_path = request.form['File_Path']
#         url = request.form['Url']
#         dict_data = {'file_path': file_path, 'url': url}
#     serverName = 'localhost'
#     serverPort = 12000
#     clientSocket = socket(AF_INET, SOCK_STREAM)
#     clientSocket.connect((serverName, serverPort))
#
#     protocol.send_data(clientSocket , data=dict_data)
#     got_data = protocol.receive_data(clientSocket)
#
#     return render_template('info.html', got_data=got_data)


if __name__ == '__main__':
    app.run()
