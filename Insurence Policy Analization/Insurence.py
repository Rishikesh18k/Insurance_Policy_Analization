from customtkinter import *
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import warnings
win = CTk()
win.title("Insurence Policy Analization")
win.geometry("343x455+500+50")
win.resizable(False, False)
win.config(bg="#333333")
# /////////////////////////////////////
def get_value():
    warnings.filterwarnings("ignore")
    area_x = eval(area_value.get())
    file = pd.read_csv("C:\\Users\\Rishikesh\\OneDrive\\Desktop\\Machine Models\\Insurence Policy Analization\\insurance_data.csv")
    age = file[["age"]]
    Eligibility = file["bought_insurance"]
    train_x,test_x,train_y,test_y=train_test_split(age,Eligibility)
    model = LogisticRegression()
    model.fit(train_x,train_y)
    prediction_value = model.predict([[area_x]])
    score_price = model.score(test_x,test_y)
    score = (score_price*100)
    if score < 0:
       percentage_value.configure(text="0.00%",text_color="#F5F5FA",font=("Franklin Gothic Demi Cond",20))
    else:
        percentage_value.configure(text=f"{round(score,0)}0%",text_color="#F5F5FA",font=("Franklin Gothic Demi Cond",20))
    if int(prediction_value[0]) >= 1:
        status_value.configure(text="Will buy",text_color="#F5F5FA",font=("Franklin Gothic Demi Cond",18))
    else:
        status_value.configure(text="Will not buy",text_color="#F5F5FA",font=("Franklin Gothic Demi Cond",18))
def clear():
    entry_label.delete(0,END)
    status_value.configure(text="----------",font=("Franklin Gothic Demi Cond",22),text_color="#737373")
    percentage_value.configure(text="000%",font=("Franklin Gothic Demi Cond",22),text_color="#737373")
# /////////////////////////////////////////////////////////////////////////////////////////
message_label = CTkLabel(win,text="Enter  your  age",font=("Franklin Gothic Demi Cond",22),
                        text_color="#EEEEEE",fg_color="#333333")
message_label.place(x=98,y=46)
message_label_1 = CTkLabel(win,text="⬇",font=("Franklin Gothic Demi Cond",20),
                        text_color="#EEEEEE",fg_color="#333333")
message_label_1.place(x=235,y=50)
area_value = StringVar()
entry_label = CTkEntry(win,text_color="#EEEEEE",font=("Franklin Gothic Demi Cond",18),bg_color="#333333",
                       height=35,width=246,border_width=1.50,border_color="#737373",
                       corner_radius=4,fg_color="#444444",textvariable=area_value)
entry_label.place(x=50,y=90)
done_btn = CTkButton(win,text="Done",font=("Franklin Gothic Demi Cond",20),height=40,
                       width=120,text_color="#FFFFFF",fg_color="#009900",corner_radius=4,
                       border_color="#EEEEEE",border_width=1,hover_color="#00cc00",
                       cursor="hand2",command=get_value)
done_btn.place(x=50,y=145)
clear_btn = CTkButton(win,text="Clear",font=("Franklin Gothic Demi Cond",18),height=40,
                       width=120,text_color="#000000",fg_color="#EEEEEE",corner_radius=4,
                       border_color="#EEEEEE",border_width=1,hover_color="#ffffff",
                       cursor="hand2",command=clear)
clear_btn.place(x=176,y=145)
details_frame = CTkFrame(win,width=246,height=195,fg_color="#404040",border_width=2,border_color="#737373",bg_color="#333333")
status_tittle = CTkLabel(details_frame,text="______Status______",font=("Franklin Gothic Demi Cond",17),width=242,text_color="#d9d9d9")
status_tittle.place(x=2,y=15)
status_value = CTkLabel(details_frame,text="----------",font=("Franklin Gothic Demi Cond",22),width=242,text_color="#737373")
status_value.place(x=2,y=55)
percentage_tittle = CTkLabel(details_frame,text="______Accurate (%)______",font=("Franklin Gothic Demi Cond",17),width=242,text_color="#d9d9d9")
percentage_tittle.place(x=2,y=100)
percentage_value = CTkLabel(details_frame,text="000%",font=("Franklin Gothic Demi Cond",22),width=242,text_color="#737373")
percentage_value.place(x=2,y=140)
details_frame.place(x=50,y=210)
win.mainloop()