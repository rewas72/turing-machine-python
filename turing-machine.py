def turing_machine_tape_simulation(user_pin, system_pin):
    tape = ['#'] + list(user_pin) + ['#'] + list(system_pin) + ['#']
    head = 1
    state = 'q1'
    index = 0  # PIN karakter eşleştirmesi için pozisyon

    print("\n--- Turing Makinesi Başlatıldı ---")
    print("Başlangıç Bandı:", ''.join(tape))

    while state not in ['ACCEPT', 'REJECT']:
        symbol = tape[head]

        if state == 'q1':
            if symbol.isdigit():
                # Sistem PIN'deki karşılık gelen rakamı bul
                system_index = len(user_pin) + 2 + index  # sistem PIN başlangıç indexi: len(pin)+2
                if symbol == tape[system_index]:
                    # Eşleşiyorsa işaretle
                    tape[head] = 'X'
                    tape[system_index] = 'Y'
                    head += 1
                    index += 1
                    state = 'q1'  # Devam et
                else:
                    state = 'REJECT'
            elif symbol == '#':
                state = 'ACCEPT'
            else:
                state = 'REJECT'

        print("Durum:", state, "| Bant:", ''.join(tape), "| Başlık Poz:", head)

    print("--- Turing Makinesi Durdu ---")
    return "\n Şifre doğru." if state == 'ACCEPT' else "\n Şifre hatalı."


if __name__ == "__main__":
    print("PIN doğrulama için 4 haneli bir PIN giriniz.")
    user_input = input("PIN kodu (4 haneli): ")
    system_pin = "1234"

    if len(user_input) == 4 and user_input.isdigit():
        result = turing_machine_tape_simulation(user_input, system_pin)
        print(result)
    else:
        print("\n⚠️ Hatalı giriş. Lütfen 4 haneli rakam giriniz.")
