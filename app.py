from customtkinter import *
import main

#Cretate window
app=CTk(fg_color='#1F456E')
app.geometry("1920x1080")
app.title("Web Application Forensics Tool")
#Icon Remaining
# app.iconphoto(False,icon)

#Appearance
set_appearance_mode("system")
set_default_color_theme("dark-blue")

#Active Scan Output Function
def active_scan_output():
    output=main.active(active_domain.get(),url.get())
    o=CTkLabel(master=tabview.tab("Active Scanning"),text=output)
    o.pack()
    return o

def pas_scan_res():
    output=main.passive(passive_domain.get())
    o=CTkLabel(master=tabview.tab("Passive Scanning"),text=output)
    o.pack()
    return o
    # print(output)



#Heading 
heading=CTkLabel(master=app,text="WebApp Forensic Tool",font=("Arial Black",24))
heading.pack(pady=20,padx=10)


tabview = CTkTabview(master=app,height=1200,width=1200,corner_radius=20,fg_color='#FC9483')
tabview.pack(padx=90, pady=50)

tabview.add("Active Scanning")  # add tab at the end
tabview.add("Passive Scanning")  # add tab at the end
tabview.set("Active Scanning")  # set currently visible tab


#Active Scan Tab
active_domain=CTkEntry(master=tabview.tab("Active Scanning"),placeholder_text="Enter domain to scan",width=900,height=40,font=("Arial",18))
active_domain.pack(padx=20,pady=20)
url=CTkEntry(master=tabview.tab("Active Scanning"),placeholder_text="Enter URl to enumerate",width=900,height=40,font=("Aria Black",18))
url.pack()
active_button = CTkButton(master=tabview.tab("Active Scanning"),text="Start Scan",height=50,width=100,font=("Arial Black",18),command=active_scan_output)
active_button.pack(padx=20, pady=20)



#Passive Scan Tab
passive_domain=CTkEntry(master=tabview.tab("Passive Scanning"),placeholder_text="Enter domain to scan",width=900,height=40,font=("Arial",18))
passive_domain.pack(pady=10)
passve_button=CTkButton(master=tabview.tab("Passive Scanning"),text="Start Scan",height=50,width=100,font=("Arial Black",18),command=pas_scan_res)
passve_button.pack()



app.mainloop()
