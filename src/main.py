from Keylogger import KeyLogger
import keyboard

# KEY_DOWN
# KEY_UP
# KeyboardEvent
# _Event
# _GenericListener
# _KeyboardListener
# _Lock
# _State
# _Thread
# _UninterruptibleEvent
# __builtins__
# __cached__
# __doc__
# __file__
# __loader__
# __name__
# __package__
# __path__
# __spec__
# _add_hotkey_step
# _canonical_names
# _collections
# _generic
# _hooks
# _hotkeys
# _is_list
# _is_number
# _is_str
# _itertools
# _keyboard_event
# _listener
# _logically_pressed_keys
# _modifier_scan_codes
# _os_keyboard
# _physically_pressed_keys
# _platform
# _pressed_events
# _pressed_events_lock
# _print_function
# _queue
# _re
# _recording
# _time
# _winkeyboard
# _word_listeners
# add_abbreviation
# add_hotkey
# add_word_listener
# all_modifiers
# block_key
# call_later
# clear_all_hotkeys
# clear_hotkey
# get_hotkey_name
# get_typed_strings
# hook
# hook_key
# is_modifier
# is_pressed(key) - Проверяет, нажата ли конкретная клавиша
# key_to_scan_codes
# normalize_name
# on_press
# on_press_key
# on_release
# on_release_key
# parse_hotkey
# parse_hotkey_combinations
# play
# press(key) - Нажимает и удерживает нажатой заданную клавишу
# press_and_release
# read_event
# read_hotkey
# read_key
# record
# register_abbreviation
# register_hotkey
# register_word_listener
# release
# remap_hotkey
# remap_key
# remove_abbreviation
# remove_all_hotkeys
# remove_hotkey
# remove_word_listener
# replay
# restore_modifiers
# restore_state
# send
# sided_modifiers
# start_recording
# stash_state
# stop_recording
# unblock_key
# unhook
# unhook_all
# unhook_all_hotkeys
# unhook_key
# unregister_all_hotkeys
# unregister_hotkey
# unremap_hotkey
# unremap_key
# version
# wait
# write

# Взаимодействие с клавиатурой:
#
# is_pressed(key): Проверяет, нажата ли конкретная клавиша (например, 'a', 'esc'). Возвращает True, если нажата, False - если нет.
# press(key): Нажимает и удерживает нажатой заданную клавишу.
# release(key): Отпускает ранее нажатую клавишу.
# press_and_release(key): Нажимает клавишу, а затем сразу же ее отпускает (имитирует нажатие клавиши).
# send(key): Отправляет нажатие клавиши, как будто она была нажата пользователем (комбинирует нажатие и отпускание).
# write(text): Набирает заданный текст посимвольно, имитируя ввод пользователя.

# Управление горячими клавишами:
#
# add_hotkey(hotkey, callback): Назначает комбинацию горячих клавиш (например, 'ctrl+shift+a') для запуска определенной функции (callback).
# remove_hotkey(hotkey): Удаляет ранее зарегистрированную горячую клавишу.
# get_hotkey_name(hotkey): Возвращает понятное человеку имя зарегистрированной горячей клавиши (если доступно).
# clear_all_hotkeys(): Удаляет все зарегистрированные горячие клавиши.
# remap_hotkey(old_hotkey, new_hotkey): Изменяет комбинацию клавиш для существующей горячей клавиши.
# unremap_hotkey(hotkey): Отменяет функциональность горячей клавиши, но не удаляет ее (можно переназначить позже).

app = KeyLogger()

app.run()

# keyboard.add_abbreviation('hw', "Abbreiation")
# keyboard.wait('esc') # ожидает нажатие клавиши
#
# keyboard.press_and_release('left windows + r')






