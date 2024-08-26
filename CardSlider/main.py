import flet as ft

def main(page: ft.Page):
    page.title = 'Card'
    page.window.width = 350
    page.window.min_width = 350
    page.window.height = 650
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.colors.GREEN
    page.padding = ft.padding.only(
        left=10,
        right=10,
        top=2,
        bottom=2
    )

    #Definindo as variaveis
    width: float = page.width
    height: float = page.height

    values = {
        "1": {
            'src': 'Designer.jpg',
            'text': 'Aprenda as técnicas modernas de design para criar apps atrativas e sair por cima do web design',
            'course': 'Designer',
            'btn_color': ft.colors.PINK
        },
        "2": {
            'src': 'Fullstack.jpeg',
            'text': 'Aprenda a programar tanto no client side como no server side. Seja um programador completo',
            'course': 'Full Stack',
            'btn_color': ft.colors.BLUE
        },
        "3": {
            'src': 'webdeveloper.jpeg',
            'text': 'Curso completo das ferramentas essenciais para o desenvolvimento web. Aprenda tags Html, CSS e JS',
            'course': 'Developer',
            'btn_color': ft.colors.GREEN
        },
    }

    # Função para colocar cor nos pontos de navegação
    def clicked(e: ft.ControlEvent):
        for control in e.control.parent.controls:
            control: ft.Container

            if control != e.control:
                control.bgcolor = ft.colors.TRANSPARENT
            
            else:
                control.bgcolor = ft.colors.BLUE
        
        page.update()

    class Card(ft.Container):
        def __init__(
            self,
            src_image: str,
            text: str,
            btn_color: str,
            course: str
        ):
            super().__init__()
            self.width = 291.67
            self.height = height * 0.48
            self.bgcolor = ft.colors.WHITE
            self.border_radius=10
            self.border = ft.border.all(
                width=1,
                color=ft.colors.BLUE
            )
            self.padding = ft.padding.all(10)
            self.content = ft.Column(
                controls=[
                    ft.Image(
                        src=src_image,
                        border_radius=10,
                        aspect_ratio=16/9,
                        fit=ft.ImageFit.COVER
                    ),
                    ft.ElevatedButton(
                        text=course,
                        color=btn_color,
                        bgcolor=ft.colors.with_opacity(0.2, btn_color),
                        height=35
                    ),
                    ft.Text(
                        value=text,
                        size=15,
                        color=ft.colors.with_opacity(0.8, 'black'),
                        weight='bold',
                        text_align=ft.TextAlign.JUSTIFY
                    ),
                    ft.IconButton(
                        icon=ft.icons.ARROW_CIRCLE_RIGHT,
                        icon_color=btn_color,
                        focus_color=ft.colors.BLUE,
                        icon_size=22
                    )
                ],
                spacing=5
            )
    
    control = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    Card(
                        src_image=values[value]['src'],
                        text=values[value]['text'],
                        btn_color=values[value]['btn_color'],
                        course=values[value]['course']
                    ) for value in values.keys()
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                controls=[
                    ft.Container(
                        width=15,
                        height=15,
                        border_radius=30,
                        border=ft.border.all(
                            width=2,
                            color=ft.colors.GREY
                        ),
                        on_click=lambda e: clicked(e)
                    ) for _ in values.keys()
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    def on_resize(e):
        width: float = page.width

        control.controls[0].width = width

        page.update()

    page.on_resized.subscribe(on_resize)
    page.add(control)

if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')