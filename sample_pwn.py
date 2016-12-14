import mylib

struct="""
struct msg
{
  __int64 post_id;
  _QWORD *sender;
  char msg[128];
  post *next;
};
struct user
{
  _QWORD name;
  __int64 priv_post;
  _QWORD next_user;
};
"""
f=open("peda-structs","w")
f.write(struct)
f.close()

debug="""
deactive alarm
deactive sleep
b*0xdeadbeef
"""
filename=""
f=open("peda-cmd","w")

def doexploit():
	sock("localhost",4000)
  ....
