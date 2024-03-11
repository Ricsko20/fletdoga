import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Text(value="Hello World!", color="lightblue"),
    )

    page.add(
        ft.Container(
            content=ft.Text(value = "A"), 
            alignment=ft.alignment.center, 
            height=200,
            margin=0,
            bgcolor="lightblue",
        )
    )

    page.add(
        ft.Container(
            content = ft.Row(
                ft.Container(height=200, width=200, bgcolor=ft.colors.YELLOW),
                ft.Container(height=200, width=200, bgcolor=ft.colors.BLUE),
                ft.Container(height=200, width=200, bgcolor=ft.colors.GREEN),
                ft.Container(height=200, width=200, bgcolor=ft.colors.BLACK),
                ft.Container(height=200, width=200, bgcolor=ft.colors.RED,
            )
        )
    )
    )
    page.update()

if __name__ == "__main__":
    ft.app(target=main)