import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'cookies': '_device_id=42e0d7ddcf37f903ace3e9064af9169c; _octo=GH1.1.159128532.1680229720; user_session=CNN_jdiX'
               '0rgTdG39KnG0eLXN6oO43l-U2JA0OAPKT18JCFEg; __Host-user_session_same_site=CNN_jdiX0rgTdG39KnG0eLXN6oO43'
               'l-U2JA0OAPKT18JCFEg; logged_in=yes; dotcom_user=y1nglun; has_recent_activity=1; color_mode=%7B%22colo'
               'r_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22ligh'
               't%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; prefer'
               'red_color_mode=light; tz=Asia%2FShanghai; _gh_sess=6qawrLGEgCZEns6YXqeaZH2s67%2BVaAxW6lzOiWhxCFAjPhmrs'
               'Nn1sshbylhHdtqEFygWifw8vf2iSkpjAHf%2BG065KXiChOQHeZ11IAchvMrPIU2I2kBp79%2F5%2BHgGWJLtDB0GlvDMg%2Fw%2FN'
               'DYxCkAUTJnHx6QFZfONo7gRkayaFY9eW7gR7%2Fpw1gUKX5CPofE%2FEjIRQIN2QEiLEhbe2LRRW9cMFxbvqyuU7butOLK6QO1jKfz'
               'aznSm7EawFRQFmnC9ecLrdjkO%2B8s%2BovYfyz6dvESMpL7ezZReMHrfFgWG9YpGtFy0fVK4gN8%3D--XZngfWWH3aLomeuw--vTQ'
               'FOgdo0DCL%2B1qWkt2u1A%3D%3D'    
}
response = requests.get('https://github.com', headers=headers)
print(response.text)
