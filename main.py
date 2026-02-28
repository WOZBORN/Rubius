import db

db.init_db()

# db.add_debt("МКК ЗаймВсемБезПроцентовКоллекторовНеБудетКлянемся", "22.02.2026", 1000000)
db.delete_debt(3)


for debt in db.get_debts():
    print(debt)