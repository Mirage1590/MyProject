import numpy as np
import streamlit as st

def intro():
    import streamlit as st
    from PIL import Image

    st.write("# Welcome to Shirt Shop! 👋")
    st.sidebar.success("Select a Page above.")

    st.markdown(
        """
        This is my project for studying in the final semester of the first year student. I'm glad you came to see my work. 
        Now, let me introduce myself. My name is Pannawit Jitpimonwat ( 65114540365 ) Bachelor's Degree students in the First Year, 
        Data Science and Software Innovation, Faculty of Science Ubon Ratchathani University.

        **👈 Please select the shirt size from the drop down on the left. To see the size and type of the shirt you want to wear!
        """
    )
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        x = Image.open('T Shirt.jpg')
        st.image(x, caption='T Shirt')
    with col2:
        y = Image.open('Sweater.jpg')
        st.image(y, caption='Sweater')
    with col3:
        z = Image.open('Hooded.jpg')
        st.image(z, caption='Hooded')
    with col4:
        q = Image.open('Jacket.jpg')
        st.image(q, caption='Jacket')
    col5, col6, col7, col8 = st.columns(4)
    with col5:
        w = Image.open('Linen.jpg')
        st.image(w, caption='Linen')
    with col6:
        e = Image.open('Polo.jpg')
        st.image(e, caption='Polo')
    with col7:
        r = Image.open('Shirt.jpg')
        new_r = r.resize((300, 300))
        st.image(new_r, caption='Office Shirt')
    with col8:
        t = Image.open('Sport.jpg')
        new_t = t.resize((300, 300))
        st.image(new_t, caption='Sport')

def mapping_demo():
    import streamlit as st

    st.write("# Shirt Type!")

    st.markdown(
        """
       **1.เสื้อยืดแขนสั้น (T-Shirt)**
        """
    )
    st.image('Type T Shirt.jpg')
    st.markdown(
        """
        เสื้อที่ผู้ชายทุกคนต้องมีติดตู้ เพราะเป็นชนิดที่ถูกหยิบมาใช้งานเป็นประจำ และเป็นทั้งชุดสบาย ๆ อยู่บ้าน หรือจะใส่ออกไปเดินเล่นเท่ ๆ ก็ได้ มีทั้งแบบเสื้อยืดผ้าฝ้าย 100 เปอร์เซ็นต์ และผ้าฝ้ายบวกผ้าใยสังเคราะห์ที่บางและระบายอาการได้ดีกว่า
        """
    )
    st.markdown(
        """
       **2.เสื้อยืดแขนยาว (Sweater)**
        """
    )
    st.image('Type Sweater.jpg')
    st.markdown(
        """
        เสื้ออีกประเภทที่หยิบมาใส่ได้ง่าย แต่ให้เอกลักษณ์การแต่งตัวแตกต่างโดยสิ้นเชิง เหมาะสำหรับคนที่อยากปิดช่วงแขนของตัวเองเพื่อซ่อนสรีระ หรือเพื่อความสวยงาม  แถมยังมีหลายประเภทให้เลือกทั้งแบบแฟชั่น แบบสปอร์ต ถือเป็นไอเทมคูล ๆ ที่แมตซ์กับอะไรก็เข้ากันดี
        """
    )
    st.markdown(
        """
       **3.เสื้อฮูด (Hoodies)**
        """
    )
    st.image('Type Hoodies.jpg')
    st.markdown(
        """
        Hoodies คือหนึ่งในเสื้อฮู้ดที่เราเห็นผ่านตาบ่อยครั้งในยุคปัจจุบัน ซึ่งเป็นผลมาจากแบรนด์ Fast-Fashion ที่ปล่อยคอลเลกชันออกมาอย่างต่อเนื่อง อย่างไรก็ตาม Everyday Hoodies มักจะเป็นเสื้อฮู้ดที่มาพร้อมฟังก์ชันสำหรับใช้งาน เช่นเนื้อผ้า Polyester ที่เคลือบสารสะท้อนรังสียูวีหรือป้องกันน้ำ โดยแบรนด์ที่แนะนำคือ Uniqlo, H&M, Zara และ The North Face
สำหรับหนุ่ม ๆ ที่กำลังมองหาเสื้อฮู้ดให้กับตัวเอง ลองนำเทคนิคในการเลือกและประเภทของเสื้อฮู้ดที่เราแนะนำมาใช้ร่วมประกอบในการตัดสินใจได้ เพราะเราเชื่อว่า Hoodies คืออีกหนึ่งไอเทมคลาสสิกที่สร้างสไตล์ที่แตกต่างให้กับผู้ชายทุกคนได้อย่างแน่นอน
        """
    )
    st.markdown(
        """
       **4.เสื้อโปโล (Polo Shirt)**
        """
    )
    st.image('Type Polo.jpg')
    st.markdown(
        """
        สำหรับผู้ชายที่ชอบแต่งตัวสบาย ๆ แต่ดูดีมีสไตล์ “โปโล” เป็นเสื้ออีกชนิดที่ควรมีติดตู้เสื้อผ้า เพราะใส่ง่ายและช่วยให้ดูสุภาพมากกว่าเสื้อยืด แม้จะเป็นคอปก แต่สวมแล้วไม่ร้อน ไม่ว่าจะใส่ทำกิจกรรมอะไรก็ดูดีได้
        """
    )
    st.markdown(
        """
       **5.เสื้อเชิ้ตทำงาน (Office Shirt)**
        """
    )
    st.image('Type OFFice.jpg')
    st.markdown(
        """
        สำหรับคนที่จำเป็นต้องแต่งตัวทางการ ไปทำงานทุกวัน เชิ้ตทำงาน ที่ออกแบบสำหรับชุดทางการ เป็นเสื้ออีกชนิดที่ควรมี เพราะช่วยเสริมลุคให้คุณดูภูมิฐาน บุคลิกน่าเชื่อถือและยังเหมาะกับการใส่คู่กับเนคไทด้วย
        """
    )
    st.markdown(
        """
       **6.เสื้อผ้าลินิน (Linen Shirt)**
        """
    )
    st.image('Type Linen.jpg')
    st.markdown(
        """
        ใครที่เหงื่อเยอะ รักแร้เปียกเป็นประจำเสื้อผ้าลินิน คือทางออกของคุณอย่างแท้จริง เชิ้ตชนิดนี้ถูกออกแบบขึ้นมาสำหรับใส่ในอากาศร้อนโดยเฉพาะ แถมเนื้อผ้ายังมีน้ำหนักเบาช่วยให้เคลื่อนไหวได้อย่างคล่องตัว โดยเฉพาะสีขาวและสีฟ้าถือเป็นสีแรก ๆ ที่ต้องมี เพราะสวมใส่ง่ายเหมาะกับหลายโอกาส
        """
    )
    st.markdown(
        """
       **7.เสื้อกีฬา (Sport Shirt)**
        """
    )
    st.image('Type Sport.jpg')
    st.markdown(
        """
        เสื้อที่ขาดไม่ได้สำหรับคนชอบออกกำลัง รวมถึงคนที่ชอบใส่เสื้อผ้าง่าย ๆ ไม่ร้อน แต่ยังให้ลุคที่ดูดีอยู่ แถมมีให้เลือกหลายแบบทั้งเสื้อฟุตบอล เสื้อบาสเก็ตบอล เสื้อวิ่ง และอีกมากมาย ใครที่อยากเปลี่ยนลุคเป็นหนุ่มสปอร์ต คล่องตัว ต้องไม่พลาด
        """
    )
    st.markdown(
        """
       **8.เสื้อคลุม (Jacket)**
        """
    )
    st.image('Type Jacket.jpg')
    st.markdown(
        """
        ใครที่ชอบแต่งตัวหลายชิ้นหรือสองเลเยอร์ เสื้อคลุมหรือเสื้อแจ็คเก็ต เป็นเสื้อที่ขาดไม่ได้สำหรับตู้เสื้อผ้าของคุณ ขณะเดียวกัน เสื้อชนิดนี้ยังมีให้เลือกหลายแบบ ทั้งแจ็คเก็ตหนัง แจ็คเก็ตยีน แจ็คเก็ตสูทแบบลำลอง เป็นต้น ใครที่ใส่เสื้อตัวเดียวจนชิน ลองหันมาสวมแจ็คเก็ตทับจะช่วยเปลี่ยนสไตล์ของคุณได้เยอะเลย
        """
    )

def plotting_demo():
    import streamlit as st
    import pandas as pd
    import time

    st.markdown(f'# {list(page_names_to_funcs.keys())[1]}')
    st.write(
        """
        ในหน้านี้จะเป็นการคำนวณ Size เสื้อจากค่าที่ผู้ใช้กรอกข้อมูลเข้ามาแล้วบอทจะคำนวณ Size เสื้อที่เหทาะสมกับผู้ใช้ออกมาให้
"""
    )

    if st.button('Load Size'):
        col10, col11 = st.columns(2)
        with col10:
            st.title("Female")
            l = pd.read_csv('Datasets(Male).csv')
            st.dataframe(l)
        with col11:
            st.title("Male")
            m = pd.read_csv('DataSets(Female).csv')
            st.dataframe(m)

    if st.button('Train'):
        st.success('Train Model Success!')
    col1, col2 = st.columns(2)
    with col1:
        number = st.number_input('Chest')
    with col2:
        number1 = st.number_input('Shirt Length')

    lee = (number, number1)
    pred1 = np.asarray(lee)
    pred2 = pred1.reshape(1, -1)


    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier
    data = pd.read_csv('Datasets(Male).csv')
    X = data[['Chest', 'Shirt Length']]
    y = data['Size']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)

    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier
    data = pd.read_csv('DataSets(Female).csv')
    KG = data[['Chest', 'Shirt Length']]
    IO = data['Size']
    KG_train, KG_test, IO_train, IO_test = train_test_split(KG, IO, test_size=0.2, random_state=42)
    MoDel = DecisionTreeClassifier()
    MoDel.fit(KG_train, IO_train)

    realpre = clf.predict(pred2)
    realpre2 = MoDel.predict(pred2)
    if st.button('Male Size'):
        with st.spinner('Pls Wait ....'):
            time.sleep(2)
            st.markdown(f'Size ที่เหมาะกับคุณคือ :{realpre}')
    if st.button('Female Size'):
        with st.spinner('Pla Wait ....'):
            time.sleep(2)
            st.markdown(f'Size ที่เหมาะกับคุณคือ :{realpre2}')

    op = []
    option = st.selectbox(
        'More option?',
        ('T Shirt', 'Sweater', 'Hoodies', 'Jacket', 'Linen Shirt', 'Polo Shirt', 'Office Shirt', 'Sport Shirt')
    )
    op.append(option)
    if option == "T Shirt":
        st.markdown(
            """
           **เสื้อยืดแขนสั้น (T-Shirt)**
            """
        )
        st.image('T Shirt.jpg')
        st.markdown(
            """
            เสื้อที่ผู้ชายทุกคนต้องมีติดตู้ เพราะเป็นชนิดที่ถูกหยิบมาใช้งานเป็นประจำ และเป็นทั้งชุดสบาย ๆ อยู่บ้าน หรือจะใส่ออกไปเดินเล่นเท่ ๆ ก็ได้ มีทั้งแบบเสื้อยืดผ้าฝ้าย 100 เปอร์เซ็นต์ และผ้าฝ้ายบวกผ้าใยสังเคราะห์ที่บางและระบายอาการได้ดีกว่า
            """
        )
        st.write("เข้าชมหน้าร้านค้าได้ที่นี้ : [link](https://shopee.co.th/search?keyword=t%20shirt&trackingId=searchhint-1676983381-473d6c8f-b1e5-11ed-91f3-b47af14b9058)")
    if option == "Sweater":
        st.markdown(
            """
           **เสื้อยืดแขนยาว (Sweater)**
            """
        )
        st.image('Sweater.jpg')
        st.markdown(
            """
            เสื้ออีกประเภทที่หยิบมาใส่ได้ง่าย แต่ให้เอกลักษณ์การแต่งตัวแตกต่างโดยสิ้นเชิง เหมาะสำหรับคนที่อยากปิดช่วงแขนของตัวเองเพื่อซ่อนสรีระ หรือเพื่อความสวยงาม  แถมยังมีหลายประเภทให้เลือกทั้งแบบแฟชั่น แบบสปอร์ต ถือเป็นไอเทมคูล ๆ ที่แมตซ์กับอะไรก็เข้ากันดี
            """
        )
        st.write("เข้าชมหน้าร้านค้าได้ที่นี้ : [link](https://shopee.co.th/search?keyword=sweater&trackingId=searchhint-1676984363-90838828-b1e7-11ed-b6b7-b47af14abd6c)")
    if option == "Hoodies":
        st.markdown(
            """
           **เสื้อฮูด (Hoodies)**
            """
        )
        st.image('Hooded.jpg')
        st.markdown(
            """
            Hoodies คือหนึ่งในเสื้อฮู้ดที่เราเห็นผ่านตาบ่อยครั้งในยุคปัจจุบัน ซึ่งเป็นผลมาจากแบรนด์ Fast-Fashion ที่ปล่อยคอลเลกชันออกมาอย่างต่อเนื่อง อย่างไรก็ตาม Everyday Hoodies มักจะเป็นเสื้อฮู้ดที่มาพร้อมฟังก์ชันสำหรับใช้งาน เช่นเนื้อผ้า Polyester ที่เคลือบสารสะท้อนรังสียูวีหรือป้องกันน้ำ โดยแบรนด์ที่แนะนำคือ Uniqlo, H&M, Zara และ The North Face
    สำหรับหนุ่ม ๆ ที่กำลังมองหาเสื้อฮู้ดให้กับตัวเอง ลองนำเทคนิคในการเลือกและประเภทของเสื้อฮู้ดที่เราแนะนำมาใช้ร่วมประกอบในการตัดสินใจได้ เพราะเราเชื่อว่า Hoodies คืออีกหนึ่งไอเทมคลาสสิกที่สร้างสไตล์ที่แตกต่างให้กับผู้ชายทุกคนได้อย่างแน่นอน
            """
        )
        st.write("เข้าชมหน้าร้านค้าได้ที่นี้ : [link](https://shopee.co.th/search?keyword=hoodie&trackingId=searchhint-1676984409-abacf5a2-b1e7-11ed-aa6a-9440c93f6414)")
    if option == "Polo Shirt":
        st.markdown(
            """
           **เสื้อโปโล (Polo Shirt)**
            """
        )
        st.image('Polo.jpg')
        st.markdown(
            """
            สำหรับผู้ชายที่ชอบแต่งตัวสบาย ๆ แต่ดูดีมีสไตล์ “โปโล” เป็นเสื้ออีกชนิดที่ควรมีติดตู้เสื้อผ้า เพราะใส่ง่ายและช่วยให้ดูสุภาพมากกว่าเสื้อยืด แม้จะเป็นคอปก แต่สวมแล้วไม่ร้อน ไม่ว่าจะใส่ทำกิจกรรมอะไรก็ดูดีได้
            """
        )
        st.write("เข้าชมหน้าร้านค้าได้ที่นี้ : [link](https://shopee.co.th/search?keyword=polo&trackingId=searchhint-1676984457-c82bf444-b1e7-11ed-bdb3-0a70be6e265f)")
    if option == "Office Shirt":
        st.markdown(
            """
           **เสื้อเชิ้ตทำงาน (Office Shirt)**
            """
        )
        st.image('Shirt.jpg')
        st.markdown(
            """
            สำหรับคนที่จำเป็นต้องแต่งตัวทางการ ไปทำงานทุกวัน เชิ้ตทำงาน ที่ออกแบบสำหรับชุดทางการ เป็นเสื้ออีกชนิดที่ควรมี เพราะช่วยเสริมลุคให้คุณดูภูมิฐาน บุคลิกน่าเชื่อถือและยังเหมาะกับการใส่คู่กับเนคไทด้วย
            """
        )
        st.write("เข้าชมหน้าร้านค้าได้ที่นี้ : [link](https://shopee.co.th/search?keyword=office%20shirt&trackingId=searchhint-1676984494-de493146-b1e7-11ed-b391-2a15f6fde0b3)")
    if option == "Linen Shirt":
        st.markdown(
            """
           **เสื้อผ้าลินิน (Linen Shirt)**
            """
        )
        st.image('Linen.jpg')
        st.markdown(
            """
            ใครที่เหงื่อเยอะ รักแร้เปียกเป็นประจำเสื้อผ้าลินิน คือทางออกของคุณอย่างแท้จริง เชิ้ตชนิดนี้ถูกออกแบบขึ้นมาสำหรับใส่ในอากาศร้อนโดยเฉพาะ แถมเนื้อผ้ายังมีน้ำหนักเบาช่วยให้เคลื่อนไหวได้อย่างคล่องตัว โดยเฉพาะสีขาวและสีฟ้าถือเป็นสีแรก ๆ ที่ต้องมี เพราะสวมใส่ง่ายเหมาะกับหลายโอกาส
            """
        )
        st.write("เข้าชมหน้าร้านค้าได้ที่นี้ : [link](https://shopee.co.th/search?keyword=linen%20shirt&trackingId=searchhint-1676984542-fab4aefe-b1e7-11ed-aba7-2cea7faefa4b)")
    if option == "Sport Shirt":
        st.markdown(
            """
           **เสื้อกีฬา (Sport Shirt)**
            """
        )
        st.image('Sport.jpg')
        st.markdown(
            """
            เสื้อที่ขาดไม่ได้สำหรับคนชอบออกกำลัง รวมถึงคนที่ชอบใส่เสื้อผ้าง่าย ๆ ไม่ร้อน แต่ยังให้ลุคที่ดูดีอยู่ แถมมีให้เลือกหลายแบบทั้งเสื้อฟุตบอล เสื้อบาสเก็ตบอล เสื้อวิ่ง และอีกมากมาย ใครที่อยากเปลี่ยนลุคเป็นหนุ่มสปอร์ต คล่องตัว ต้องไม่พลาด
            """
        )
        st.write("เข้าชมหน้าร้านค้าได้ที่นี้ : [link](https://shopee.co.th/search?keyword=sport%20shirt&trackingId=searchhint-1676984576-0f777e7f-b1e8-11ed-b391-2a15f6fde0b3)")
    if option == "Jacket":
        st.markdown(
            """
           **เสื้อคลุม (Jacket)**
            """
        )
        st.image('Jacket.jpg')
        st.markdown(
            """
            ใครที่ชอบแต่งตัวหลายชิ้นหรือสองเลเยอร์ เสื้อคลุมหรือเสื้อแจ็คเก็ต เป็นเสื้อที่ขาดไม่ได้สำหรับตู้เสื้อผ้าของคุณ ขณะเดียวกัน เสื้อชนิดนี้ยังมีให้เลือกหลายแบบ ทั้งแจ็คเก็ตหนัง แจ็คเก็ตยีน แจ็คเก็ตสูทแบบลำลอง เป็นต้น ใครที่ใส่เสื้อตัวเดียวจนชิน ลองหันมาสวมแจ็คเก็ตทับจะช่วยเปลี่ยนสไตล์ของคุณได้เยอะเลย
            """
        )
        st.write("เข้าชมหน้าร้านค้าได้ที่นี้ : [link](https://shopee.co.th/search?keyword=jacket%20shirt&trackingId=searchhint-1676984601-1e4d28c0-b1e8-11ed-bce7-2cea7fc2d820)")







page_names_to_funcs = {
    "Home Page": intro,
    "Shirt Size": plotting_demo,
    "Shirt Type": mapping_demo,
}

demo_name = st.sidebar.selectbox("Choose a Page", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()