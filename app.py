import numpy as np
import streamlit as st

dictionary_mark_model = {
    'Opel': ['adam', 'agila', 'ampera', 'antara', 'astra', 'combo', 'corsa', 'crossland-x', 'frontera', 'grandland-x',
             'insignia', 'karl', 'meriva', 'mokka', 'omega', 'signum', 'tigra', 'vectra', 'vivaro', 'zafira'],
    'Audi': ['80', 'a1', 'a2', 'a3', 'a4', 'a4-allroad', 'a5', 'a6', 'a6-allroad', 'a7', 'a8', 'e-tron', 'q2', 'q3',
             'q4-sportback', 'q5', 'q7', 'q8', 'rs3', 'rs5', 'rs6', 'rs-q3', 's3', 's5', 's8', 'sq5', 'tt'],
    'BMW': ['3gt', '5gt', 'i3', 'm2', 'm3', 'm4', 'm5', 'm8', 'seria-1', 'seria-2', 'seria-3', 'seria-4', 'seria-5',
            'seria-6', 'seria-7', 'seria-8', 'x1', 'x2', 'x3', 'x4', 'x5', 'x5-m', 'x6', 'x6-m', 'x7'],
    'Volkswagen': ['amarok', 'arteon', 'beetle', 'caddy', 'california', 'caravelle', 'cc', 'crafter', 'eos', 'fox',
                   'golf', 'golf-plus', 'golf-sportsvan', 'id4', 'jetta', 'lupo', 'multivan', 'new-beetle', 'passat',
                   'passat-cc', 'phaeton', 'polo', 'scirocco', 'sharan', 't-cross', 't-roc', 'tiguan',
                   'tiguan-allspace', 'touareg', 'touran', 'transporter', 'up'],
    'Ford': ['b-max', 'c-max', 'ecosport', 'edge', 'escape', 'explorer', 'f150', 'fiesta', 'focus', 'focus-c-max',
             'fusion', 'galaxy', 'grand-c-max', 'ka', 'kuga', 'mondeo', 'mustang', 'mustang-mach-e', 'puma', 'ranger',
             's-max', 'tourneo-connect', 'tourneo-courier', 'tourneo-custom', 'transit', 'transit-connect',
             'transit-custom'],
    'Mercedes-Benz': ['amg-gt', 'citan', 'cl-klasa', 'cla-klasa', 'clk-klasa', 'cls-klasa', 'gl-klasa', 'gla-klasa',
                      'glb-klasa', 'glc-klasa', 'gle-klasa', 'glk-klasa', 'gls-klasa', 'a-klasa', 'b-klasa', 'c-klasa',
                      'e-klasa', 'g-klasa', 'r-klasa', 's-klasa', 'v-klasa', 'm-klasa', 'sl', 'slk-klasa', 'sprinter',
                      'viano', 'vito'],
    'Renault': ['arkana', 'captur', 'clio', 'espace', 'grand-espace', 'grand-scenic', 'fluence', 'kadjar', 'kangoo',
                'koleos', 'laguna', 'megane', 'modus', 'scenic', 'talisman', 'thalia', 'trafic', 'twingo', 'zoe'],
    'Toyota': ['auris', 'avensis', 'aygo', 'c-hr', 'camry', 'corolla', 'corolla-verso', 'land-cruiser', 'prius',
               'proace-verso', 'rav4', 'sienna', 'yaris', 'verso'],
    'Skoda': ['citigo', 'enyaq', 'fabia', 'kamiq', 'karoq', 'kodiaq', 'octavia', 'rapid', 'roomster', 'scala', 'superb',
              'yeti'], 'Alfa-Romeo': ['147', '159', 'giulia', 'giulietta', 'mito'],
    'Chevrolet': ['aveo', 'camaro', 'cruze', 'orlando'],
    'Citroen': ['berlingo', 'c3-aircross', 'c3-picasso', 'c4-cactus', 'c4-grand-picasso', 'c4-picasso', 'c5',
                'c5-aircross', 'ds3', 'ds4', 'ds5', 'xsara-picasso'],
    'Fiat': ['500', '500l', '500x', 'bravo', 'doblo', 'freemont', 'grande-punto', 'panda', 'punto', 'punto-evo',
             'tipo'], 'Honda': ['accord', 'cr-v', 'hr-v', 'jazz', 'civic'],
    'Hyundai': ['elantra', 'i10', 'i20', 'i30', 'i40', 'ix20', 'ix35', 'kona', 'santa-fe', 'tucson'],
    'kia': ['carens', 'ceed', 'optima', 'picanto', 'pro-ceed', 'sorento', 'soul', 'sportage', 'stinger', 'stonic',
            'venga', 'xceed'], 'Mazda': ['2', '3', '5', '6', 'cx-3', 'cx-5', 'cx-7', 'cx-9', 'cx-30', 'mx-5'],
    'Mini': ['clubman', 'cooper', 'cooper-s', 'countryman', 'one'],
    'Mitsubishi': ['asx', 'colt', 'eclipse-cross', 'lancer', 'outlander', 'space-star'],
    'Nissan': ['almera', 'juke', 'leaf', 'micra', 'murano', 'note', 'patrol', 'primera', 'qashqai', 'qashqai-2',
               'x-trail'],
    'Peugeot': ['206', '207', '208', '307', '308', '407', '508', '2008', '3008', '5008', 'expert', 'partner'],
    'Seat': ['alhambra', 'altea', 'altea-xl', 'arona', 'ateca', 'exeo', 'ibiza', 'leon', 'toledo'],
    'Volvo': ['c30', 's40', 's60', 's80', 'v40', 'v50', 'v60', 'v70', 'v90', 'xc-40', 'xc-60', 'xc-70', 'xc-90']}

st.title("Car Price Prediction :car:")

col1, col2, col3, col4 = st.columns(4)
with col1:
    mark = st.session_state['mark'] = st.selectbox("Select your car brand", list(dictionary_mark_model.keys()))
with col2:
    selected_brand = st.session_state['mark']
    model = st.selectbox("Select your car model", dictionary_mark_model[selected_brand])
with col3:
    car_year = st.number_input("Enter your car year", min_value=1990, max_value=2024, step=1)
with col4:
    mileage = st.number_input("Enter your car mileage", min_value=0, max_value=1000000, step=1000)


def predict_price(mark_, model_, car_year_, mileage_):
    row = [mark_, model_, car_year_, mileage_]
    price = 10000
    price_string = f'{price:,}'.replace(',', ' ')

    return price_string


if st.button("Predict price"):
    st.info(f"Your car price is: {predict_price(mark, model, car_year, mileage)} PLN")
