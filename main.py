import flet as ft

def main(page: ft.Page):
    # Cấu hình form dáng ứng dụng
    page.title = "Mastering Audio"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0B1120" # Tông nền xanh đen sâu
    page.window_width = 450
    page.window_height = 850
    page.padding = 15

    # 1. Header (Thanh tiêu đề)
    header = ft.Row([
        ft.Row([
            ft.Icon(ft.icons.EQUALIZER, color="#4D96FF", size=32),
            ft.Column([
                ft.Text("Mastering Audio", size=22, weight="bold", color="#4D96FF"),
                ft.Text("Nâng tầm âm nhạc của bạn", size=13, color=ft.colors.GREY_400)
            ], spacing=0)
        ]),
        ft.IconButton(ft.icons.SETTINGS, icon_color=ft.colors.WHITE)
    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    # 2. Banner giới thiệu (Gradient)
    banner = ft.Container(
        content=ft.Column([
            ft.Text("Biến bản thu thành\nâm thanh chuyên nghiệp", size=16, weight="bold", color=ft.colors.WHITE),
            ft.Text("Tự động cân bằng, nén, tăng độ lớn,\ntối ưu hóa dải tần và làm sạch âm thanh.", size=12, color=ft.colors.GREY_400)
        ]),
        padding=20,
        border_radius=12,
        gradient=ft.LinearGradient(
            begin=ft.alignment.center_left, end=ft.alignment.center_right,
            colors=["#15234B", "#0B1120"]
        ),
        border=ft.border.all(1, "#1E2D52")
    )

    # 3. Thông tin File
    file_info = ft.Container(
        content=ft.Row([
            ft.Container(
                content=ft.Icon(ft.icons.MUSIC_NOTE, color=ft.colors.WHITE),
                bgcolor="#4D96FF", width=50, height=50, border_radius=10, alignment=ft.alignment.center
            ),
            ft.Column([
                ft.Text("Pho_xa_Acoustic.mp3", weight="bold", size=14),
                ft.Text("MP3 • 4.2 MB • 03:45", size=12, color=ft.colors.GREY_400)
            ], expand=True, spacing=2),
            ft.OutlinedButton(
                "Chọn file", 
                icon=ft.icons.FOLDER, 
                style=ft.ButtonStyle(color=ft.colors.WHITE, side=ft.BorderSide(1, ft.colors.GREY_600), shape=ft.RoundedRectangleBorder(radius=8))
            )
        ]),
        padding=10, border_radius=12, border=ft.border.all(1, "#1E2D52"), bgcolor="#101827"
    )

    # 4. Trình phát âm thanh so sánh (Trước & Sau)
    def build_player(title, subtitle, color, icon):
        return ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Icon(icon, color=color, size=20),
                    ft.Column([
                        ft.Text(title, weight="bold", size=13), 
                        ft.Text(subtitle, size=11, color=ft.colors.GREY_400)
                    ], spacing=0)
                ]),
                # Mô phỏng biểu đồ Waveform
                ft.Container(height=40, bgcolor=ft.colors.with_opacity(0.1, color), border_radius=5, alignment=ft.alignment.center, content=ft.Text("Waveform", size=10, color=color)),
                ft.Text("00:00 / 03:45", size=11, color=ft.colors.GREY_400),
                ft.Row([
                    ft.Container(
                        content=ft.Icon(ft.icons.PLAY_ARROW, color=ft.colors.WHITE if color=="#4D96FF" else ft.colors.WHITE, size=20),
                        bgcolor=color if color=="#4D96FF" else ft.colors.TRANSPARENT,
                        border=ft.border.all(1, color) if color!="#4D96FF" else None,
                        width=35, height=35, border_radius=20, alignment=ft.alignment.center
                    ),
                    ft.Icon(ft.icons.VOLUME_UP, size=16, color=ft.colors.GREY_400),
                    ft.Slider(value=60, min=0, max=100, expand=True, thumb_color=color, active_color=color)
                ])
            ], spacing=8),
            expand=True, padding=12, border=ft.border.all(1, "#1E2D52"), border_radius=12, bgcolor="#101827"
        )

    players = ft.Row([
        build_player("Audio (Original)", "Âm thanh gốc", ft.colors.GREY_400, ft.icons.HEADPHONES),
        build_player("Audio (Mastered)", "Mastering", "#4D96FF", ft.icons.AUTO_AWESOME)
    ], spacing=10)

    # 5. Nút bấm chính (Gradient)
    master_btn = ft.Container(
        content=ft.Row([
            ft.Icon(ft.icons.EQUALIZER, color=ft.colors.WHITE),
            ft.Text("Mastering ngay", weight="bold", size=16, color=ft.colors.WHITE)
        ], alignment=ft.MainAxisAlignment.CENTER),
        height=55, border_radius=27,
        gradient=ft.LinearGradient(colors=["#2196F3", "#9C27B0"]),
        on_click=lambda e: print("Bắt đầu xử lý âm thanh pydub...")
    )

    # 6. Các chế độ Mastering
    def build_mode(title, subtitle, icon, is_active=False):
        bgcolor = "#15234B" if is_active else "#101827"
        border_color = "#4D96FF" if is_active else "#1E2D52"
        return ft.Container(
            content=ft.Column([
                ft.Icon(icon, color="#4D96FF" if is_active else ft.colors.GREY_400, size=26),
                ft.Text(title, weight="bold", size=12, color=ft.colors.WHITE if is_active else ft.colors.GREY_300),
                ft.Text(subtitle, size=10, color=ft.colors.GREY_400)
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=3),
            expand=True, height=90, border_radius=12, border=ft.border.all(1, border_color), bgcolor=bgcolor
        )

    modes_text = ft.Text("Chế độ Mastering", weight="bold", size=14)
    modes_grid = ft.Row([
        build_mode("Tự động", "(Đề xuất)", ft.icons.MUSIC_NOTE, True),
        build_mode("Giọng nói", "(Podcast, Vocal)", ft.icons.MIC, False),
        build_mode("Nhạc cụ", "(Nhạc cụ đơn)", ft.icons.LIBRARY_MUSIC, False),
        build_mode("Âm nhạc", "(Nhạc tổng hợp)", ft.icons.EQUALIZER, False)
    ], spacing=10)

    # 7. Các tùy chỉnh nâng cao (Toggles)
    def build_toggle(title, subtitle, icon, active):
        return ft.Container(
            content=ft.Row([
                ft.Container(content=ft.Icon(icon, color=ft.colors.GREY_300, size=20), padding=8, bgcolor="#1A2A4A", border_radius=8),
                ft.Column([
                    ft.Text(title, weight="bold", size=12),
                    ft.Text(subtitle, size=10, color=ft.colors.GREY_400)
                ], expand=True, spacing=1),
                ft.Switch(value=active, active_color="#4D96FF")
            ]), expand=True, padding=10, border_radius=12, border=ft.border.all(1, "#1E2D52"), bgcolor="#101827"
        )

    toggles_1 = ft.Row([
        build_toggle("Cân bằng âm sắc", "Tối ưu dải tần", ft.icons.TUNE, True),
        build_toggle("Tăng độ lớn", "Đạt mức chuẩn", ft.icons.VOLUME_UP, True)
    ], spacing=10)
    
    toggles_2 = ft.Row([
        build_toggle("Nén động", "Tránh méo tiếng", ft.icons.COMPRESS, True),
        build_toggle("Giảm nhiễu", "Loại bỏ tạp âm", ft.icons.CLEANING_SERVICES, True)
    ], spacing=10)

    # 8. Thanh điều hướng cuối màn hình (Bottom Navigation Bar)
    page.navigation_bar = ft.NavigationBar(
        bgcolor="#0B1120", selected_index=0,
        destinations=[
            ft.NavigationDestination(icon=ft.icons.EQUALIZER, label="Trang chủ"),
            ft.NavigationDestination(icon=ft.icons.FOLDER_OPEN, label="Dự án"),
            ft.NavigationDestination(icon=ft.icons.HEADPHONES, label="Nghe thử"),
            ft.NavigationDestination(icon=ft.icons.PERSON_OUTLINE, label="Cá nhân"),
        ]
    )

    # Ghép tất cả các thành phần vào thân ứng dụng có thể cuộn được
    main_content = ft.Column([
        header, 
        ft.Divider(height=5, color=ft.colors.TRANSPARENT),
        banner,
        file_info,
        players,
        ft.Divider(height=10, color=ft.colors.TRANSPARENT),
        master_btn,
        ft.Container(
            content=ft.Row([
                ft.Icon(ft.icons.TUNE, color=ft.colors.GREY_400, size=20),
                ft.Text("Tùy chỉnh (nâng cao)", size=13, weight="bold"),
                ft.Container(expand=True),
                ft.Icon(ft.icons.KEYBOARD_ARROW_RIGHT, color=ft.colors.GREY_400)
            ]),
            padding=15, border_radius=8, border=ft.border.all(1, "#1E2D52")
        ),
        modes_text,
        modes_grid,
        ft.Divider(height=5, color=ft.colors.TRANSPARENT),
        toggles_1,
        toggles_2
    ], scroll=ft.ScrollMode.AUTO, expand=True, spacing=15)

    page.add(main_content)

ft.app(main)