from customtkinter import *
import main

#Cretate window
app=CTk()
app.geometry("1368x700")
app.title("Directing System Management Decision Making using Forensic Analysis of Web Applicaton")
#Icon Remaining
# app.iconphoto(False,icon)

#Appearance
set_appearance_mode("system")
set_default_color_theme("dark-blue")

#Active Scan Output Function
def active_scan_output():
    output=main.active(active_domain.get(), url.get(), port_num.get())
    output_frame = CTkScrollableFrame(master=tabview.tab("ACTIVE"), width=1000, height=500)
    output_frame.pack(padx=10,pady=10)
    o=CTkLabel(master=output_frame,text=output)
    o.pack()
    return o

def pas_scan_res():
    try:
        output=main.passive(passive_domain.get())
    except BaseException:
        output='Failed'
    output_frame = CTkScrollableFrame(master=tabview.tab("PASSIVE"), width=1000, height=500)
    # progressbar = CTkProgressBar(master=tabview.tab("Passive Scanning"))
    # progressbar.pack(padx=20, pady=10)
    output_frame.pack(padx=10,pady=10)
    o=CTkLabel(master=output_frame,text=output)
    o.pack()
    return o
    # print(output)


#Heading 
heading=CTkLabel(master=app,text="Directing System Management Decision \n Making using Forensic Analysis of Web Applicaton",font=("Arial Black",24))
heading.pack(pady=20,padx=10)


tabview = CTkTabview(master=app,height=1200,width=1200,corner_radius=20,fg_color='#B7BCBF')
tabview.pack(padx=90, pady=50)

tabview.add("ACTIVE")  # add tab at the end
tabview.add("PASSIVE")  # add tab at the end
tabview.set("ACTIVE")  # set currently visible tab


#Active Scan Tab
active_domain=CTkEntry(master=tabview.tab("ACTIVE"),placeholder_text="Enter domain to scan",width=900,height=40,font=("Arial",18))
active_domain.pack(pady=10)
url=CTkEntry(master=tabview.tab("ACTIVE"),placeholder_text="Enter URl to enumerate",width=900,height=40,font=("Arial",18))
url.pack(pady=10)
port_num=CTkEntry(master=tabview.tab("ACTIVE"), placeholder_text='Port number as 1,2,3..',width=900,height=40,font=('Arial', 18))
port_num.pack(pady=10)
active_button = CTkButton(master=tabview.tab("ACTIVE"),text="Start Scan",height=50,width=100,font=("Arial Black",18),command=active_scan_output)
active_button.pack(padx=20, pady=20)


#Passive Scan Tab
passive_domain=CTkEntry(master=tabview.tab("PASSIVE"),placeholder_text="Enter domain to scan",width=900,height=40,font=("Arial",18))
passive_domain.pack(pady=10)
passve_button=CTkButton(master=tabview.tab("PASSIVE"),text="Start Scan",height=50,width=100,font=("Arial Black",18),command=pas_scan_res)
passve_button.pack()



app.mainloop()
