import streamlit as st
from PIL import Image

st.title('1日消費カロリーメーター')
st.write('一日の消費カロリーを知って、食事や運動に生かそう！')
st.write('※これはあくまでも目安です。これを指標として、日々の運動と食事を意識しましょう！')

img = Image.open('running.jpg')
st.image(img, caption='', use_column_width=True)

def recommend_meal(calorie):
    if calorie < 1500:
        return "消費カロリーが低いため、バランスの取れた食事を心掛けよう。例えば、筑前煮など１食400kcal程度の食事がおすすめ!", "C:\\Users\\SatoDaichi\\Downloads\\筑前煮.jpg"
    elif 1500 <= calorie < 2000:
        return "消費カロリーに合わせて、野菜、たんぱく質、炭水化物をバランスよく摂取することが大切。例えば、鶏もも肉のソテーなどの１食600kcal程度の食事がおすすめ!", "C:\\Users\\SatoDaichi\\Downloads\\鶏もも肉.jpg"
    else:
        return "アスリート並みの消費カロリーのため、たんぱく質と炭水化物をしっかり取ろう。例えば、高カロリーの食事で、１食800kcal程度の食事がおすすめ！", "C:\\Users\\SatoDaichi\\Downloads\\高カロリー.jpg"

def calculate_calorie(gender, age, weight, height, activity_level):
    if gender == "男性":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

    if activity_level == 1:
        calorie = bmr * 1.2
    elif activity_level == 2:
        calorie = bmr * 1.375
    elif activity_level == 3:
        calorie = bmr * 1.55
    elif activity_level == 4:
        calorie = bmr * 1.725
    else:
        return "適切な選択肢を入力してください"

    return calorie

def main():
    gender = st.selectbox("性別を選択してください", ["男性", "女性"])
    age = st.number_input("年齢を入力してください", min_value=0, max_value=150, value=30)
    weight = st.number_input("体重(kg)を入力してください", min_value=0.0, max_value=300.0, value=60.0)
    height = st.number_input("身長(cm)を入力してください", min_value=0.0, max_value=300.0, value=170.0)
    activity_level = st.selectbox("身体レベルを選んでください",["ほとんど運動しない", "軽い運動", "運動量が普通", "運動量が高い"])

    if st.button("計算"):
        if activity_level == "ほとんど運動しない":
            activity_level = 1
        elif activity_level == "軽い運動":
            activity_level = 2
        elif activity_level == "運動量が普通":
            activity_level = 3
        elif activity_level == "運動量が高い":
            activity_level = 4

        calorie = calculate_calorie(gender, age, weight, height / 100, activity_level)
        st.write(f"あなたの消費カロリーは {calorie:.2f} kcalです。")
        
        meal_recommendation, image_path = recommend_meal(calorie)
        st.write("おすすめの食事:")
        st.write(meal_recommendation)
        
        image = Image.open(image_path)
        st.image(image, caption='おすすめの食事', use_column_width=True)

if __name__ == "__main__":
    main()

