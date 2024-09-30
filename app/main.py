import streamlit as st

if "data" not in st.session_state:
    st.session_state.data = [{"id": 1, "name": "Taro", "age": 24},
                             {"id": 2, "name": "Hanako", "age": 22},
                             {"id": 3, "name": "Jiro", "age": 30}]
if "next_id" not in st.session_state:
    st.session_state.next_id = 4

menu = st.sidebar.selectbox("メニューを選択してください",
                            ["データ一覧", "データ追加", "データ編集", "データ削除"]
                            )

# Retrieve
if menu == "データ一覧":
    st.title("データ一覧")
    st.table(st.session_state.data)

# Insert 
elif menu == "データ追加":
    st.title("データ追加")

    new_name = st.text_input("名前を入力してください")
    new_age = st.number_input("年齢を入力してください", min_value=0, step=1)

    if st.button("追加"):
        if new_name:
            new_record = {"id": st.session_state.next_id, "name": new_name, "age": new_age}
            st.session_state.data.append(new_record)
            st.session_state.next_id += 1
            st.success(f"{new_name} を追加しました！")
        else:
            st.warning("名前を入力してください")

# Update
elif menu == "データ編集":
    st.title("データ編集")

    selected_id = st.selectbox("編集するIDを選択してください", [record["id"] for record in st.session_state.data])

    if selected_id:
        record_to_edit = next((record for record in st.session_state.data if record["id"] == selected_id), None)

        if record_to_edit:
            new_name = st.text_input("名前を入力してください", record_to_edit["name"])
            new_age = st.number_input("年齢を入力してください", min_value=0, value=record_to_edit["age"], step=1)

            if st.button("保存"):
                record_to_edit["name"] = new_name
                record_to_edit["age"] = new_age
                st.success(f"ID: {selected_id} のデータを更新しました！")

# Delete
elif menu == "データ削除":
    st.title("データ削除")

    selected_id = st.selectbox("削除するIDを選択してください", [record["id"] for record in st.session_state.data])

    if selected_id:
        if st.button("削除"):
            st.session_state.data = [record for record in st.session_state.data if record["id"] != selected_id]
            st.success(f"ID: {selected_id} のデータを削除しました！")
