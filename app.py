import streamlit as st

# Настройка страницы (иконка и заголовок на смартфоне)
st.set_page_config(page_title="Калькулятор экскурсии", page_icon="🚌", layout="centered")

st.title("🚌 Расчет экскурсии")

# Создаем 3 удобные вкладки для навигации на телефоне
tab1, tab2, tab3 = st.tabs(["Общие расходы", "Сопровождающие", "На ребенка"])

with tab1:
    st.subheader("Базовые расходы")
    bus = st.number_input("Автобус:", min_value=0.0, format="%.2f")
    suburb = st.number_input("Пригород:", min_value=0.0, format="%.2f")
    quest = st.number_input("Квест:", min_value=0.0, format="%.2f")
    add_exp_1 = st.number_input("Доп. расходы 1:", min_value=0.0, format="%.2f")
    add_exp_2 = st.number_input("Доп. расходы 2:", min_value=0.0, format="%.2f")
    add_exp_3 = st.number_input("Доп. расходы 3:", min_value=0.0, format="%.2f")

    st.subheader("Экскурсионное обслуживание")
    group_count = st.number_input("Количество групп:", min_value=0, step=1)
    exc_m1 = st.number_input("Музей 1 (на группу):", min_value=0.0, format="%.2f")
    exc_m2 = st.number_input("Музей 2 (на группу):", min_value=0.0, format="%.2f")
    exc_park = st.number_input("Парк (на группу):", min_value=0.0, format="%.2f")

with tab2:
    st.subheader("Расходы на сопровождающих")
    adults_count = st.number_input("Кол-во сопровождающих:", min_value=0, step=1)
    a_m1 = st.number_input("Музей 1 (сопров-е):", min_value=0.0, format="%.2f")
    a_m2 = st.number_input("Музей 2 (сопров-е):", min_value=0.0, format="%.2f")
    a_mc = st.number_input("Мастер-класс (сопров-е):", min_value=0.0, format="%.2f")
    a_grotto = st.number_input("Гроты (сопров-е):", min_value=0.0, format="%.2f")
    a_ferry = st.number_input("Переправа (сопров-е):", min_value=0.0, format="%.2f")
    a_park_1 = st.number_input("Парк 1 (сопров-е):", min_value=0.0, format="%.2f")
    a_park_2 = st.number_input("Парк 2 (сопров-е):", min_value=0.0, format="%.2f")
    a_lunch = st.number_input("Обед (сопров-е):", min_value=0.0, format="%.2f")

with tab3:
    st.subheader("Индивидуальные расходы")
    c_museum_1 = st.number_input("Входной билет музей 1:", min_value=0.0, format="%.2f")
    c_museum_2 = st.number_input("Входной билет музей 2:", min_value=0.0, format="%.2f")
    c_park_1 = st.number_input("Входной билет парк 1:", min_value=0.0, format="%.2f")
    c_park_2 = st.number_input("Входной билет парк 2:", min_value=0.0, format="%.2f")
    c_fort = st.number_input("Форт:", min_value=0.0, format="%.2f")
    c_mc = st.number_input("Мастер-класс:", min_value=0.0, format="%.2f")
    c_grotto = st.number_input("Гроты:", min_value=0.0, format="%.2f")
    c_lunch = st.number_input("Обед:", min_value=0.0, format="%.2f")
    c_ferry = st.number_input("Переправа:", min_value=0.0, format="%.2f")
    c_train = st.number_input("Паровозик:", min_value=0.0, format="%.2f")

st.divider() # Горизонтальная линия

# === МАТЕМАТИКА ===
exc_total = (exc_m1 + exc_m2 + exc_park) * group_count
base_shared_cost = bus + suburb + quest + add_exp_1 + add_exp_2 + add_exp_3 + exc_total

adults_expenses = a_mc + a_grotto + a_ferry + a_park_1 + a_park_2 + a_lunch + a_m1 + a_m2
total_adults_cost = adults_expenses * adults_count

total_shared_cost = base_shared_cost + total_adults_cost
child_personal_cost = c_mc + c_park_1 + c_park_2 + c_museum_1 + c_museum_2 + c_fort + c_grotto + c_lunch + c_ferry + c_train

# === ВЫВОД РЕЗУЛЬТАТОВ ===
st.header("ИТОГИ")
st.info(f"**Общие расходы (до деления):** {total_shared_cost:.2f} руб.")

groups = [20, 25, 30, 35, 40, 45]
# На телефоне колонки автоматически выстроятся друг под другом, а на ПК будут в 2 ряда
cols = st.columns(2)

for i, g in enumerate(groups):
    price = (total_shared_cost / g) + child_personal_cost if g > 0 else 0
    with cols[i % 2]:
        st.success(f"**Группа {g} детей:**\n\n{price:.2f} руб.")