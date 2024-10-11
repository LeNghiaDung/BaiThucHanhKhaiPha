import tkinter as tk
from tkinter import messagebox
import pickle


with open ('D:\VSCcode\Python\Bài thực hành.ipynb (1).pkl', 'rb') as file: model = pickle.load(file)

def predict():
    try:
        input_feature = [
            float(enty_fixed_acidity.get()),
            float(enty_volatile_acidity.get()),
            float(enty_citric_acid.get()),
            float(enty_residual_sugar.get()),
            float(enty_chlorides.get()),
            float(enty_free_sulfur_dioxide.get()),
            float(enty_total_sulfur_dioxide.get()),
            float(enty_pH.get()),
            float(enty_sulphates.get()),
            float(enty_alcohol.get()),
            float(enty_quality.get())
        ]
        
        # gia tri du doan
        
        prediction = model.predict([input_feature])
        
        messagebox.showinfo("Kết quả dự đoán", f"Dự đoán: {prediction[0]}")
                            
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng giá trị")
        
root = tk.Tk()
root.title("Dự đoán chất lượng rượu")

enty_fixed_acidity = tk.Entry(root, width=30)
enty_fixed_acidity.grid(row=0, column=1)

enty_volatile_acidity = tk.Entry(root, width=30)
enty_volatile_acidity.grid(row=1, column=1)

enty_citric_acid = tk.Entry(root, width=30)
enty_citric_acid.grid(row=2, column=1)

enty_residual_sugar = tk.Entry(root, width=30)
enty_residual_sugar.grid(row=3, column=1)

enty_chlorides = tk.Entry(root, width=30)
enty_chlorides.grid(row=4, column=1)

enty_free_sulfur_dioxide = tk.Entry(root, width=30)
enty_free_sulfur_dioxide.grid(row=5, column=1)

enty_total_sulfur_dioxide = tk.Entry(root, width=30)
enty_total_sulfur_dioxide.grid(row=6, column=1)

enty_pH = tk.Entry(root, width=30)
enty_pH.grid(row=7, column=1)

enty_sulphates = tk.Entry(root, width=30)
enty_sulphates.grid(row=8, column=1)

enty_alcohol = tk.Entry(root, width=30)
enty_alcohol.grid(row=9, column=1)

enty_quality = tk.Entry(root, width=30)
enty_quality.grid(row=10, column=1)

#Tạo nút dự đoán
btn_predict = tk.Button(root, text="Dự đoán", command=predict)
btn_predict.grid(row=11, column=1)

root.mainloop()