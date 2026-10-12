import streamlit as st

# Настройка страницы (иконка и заголовок на смартфоне)
st.set_page_config(page_title="Калькулятор экскурсии", page_icon="🚌", layout="centered")

st.title("🚌 Расчет экскурсии")

# Вспомогательная функция для идеального мобильного ввода
def get_number(label):
    # Используем text_input, чтобы поле было пустым, без лишних нулей и без кнопок +/-
    val = st.text_input(label, value="", placeholder=" ")
    if val:
        try:
            # Автоматически меняем запятую на точку и убираем случайные пробелы
            return float(val.replace(',', '.').replace(' ', ''))
        except ValueError:
            st.error(f"Пожалуйста, введите корректное число в поле '{label}'")
            return 0.0
    return 0.0

# Создаем 3 удобные вкладки для навигации на телефоне
tab1, tab2, tab3 = st.tabs(["Общие расходы", "Сопровождающие", "На ребенка"])

with tab1:
    st.subheader("Базовые расходы")
    bus = get_number("Автобус:")
    suburb = get_number("Пригород:")
    quest = get_number("Квест:")
    add_exp_1 = get_number("Доп. расходы 1:")
    add_exp_2 = get_number("Доп. расходы 2:")
    add_exp_3 = get_number("Доп. расходы 3:")

    st.subheader("Экскурсионное обслуживание")
    group_count = get_number("Количество групп:")
    exc_m1 = get_number("Музей 1 (на группу):")
    exc_m2 = get_number("Музей 2 (на группу):")
    exc_park = get_number("Парк (на группу):")

with tab2:
    st.subheader("Расходы на сопровождающих")
    adults_count = get_number("Кол-во сопровождающих:")
    a_m1 = get_number("Музей 1 (сопров-е):")
    a_m2 = get_number("Музей 2 (сопров-е):")
    a_mc = get_number("Мастер-класс (сопров-е):")
    a_grotto = get_number("Гроты (сопров-е):")
    a_ferry = get_number("Переправа (сопров-е):")
    a_park_1 = get_number("Парк 1 (сопров-е):")
    a_park_2 = get_number("Парк 2 (сопров-е):")
    a_lunch = get_number("Обед (сопров-е):")

with tab3:
    st.subheader("Индивидуальные расходы")
    c_museum_1 = get_number("Входной билет музей 1:")
    c_museum_2 = get_number("Входной билет музей 2:")
    c_park_1 = get_number("Входной билет парк 1:")
    c_park_2 = get_number("Входной билет парк 2:")
    c_fort = get_number("Форт:")
    c_mc = get_number("Мастер-класс:")
    c_grotto = get_number("Гроты:")
    c_lunch = get_number("Обед:")
    c_ferry = get_number("Переправа:")
    c_train = get_number("Паровозик:")

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
cols = st.columns(2)

for i, g in enumerate(groups):
    # Расчет производим, только если введено хоть какое-то количество детей, чтобы избежать ошибок деления на 0
    price = (total_shared_cost / g) + child_personal_cost if g > 0 else 0
    with cols[i % 2]:
        st.success(f"**Группа {g} детей:**\n\n{price:.2f} руб.")
