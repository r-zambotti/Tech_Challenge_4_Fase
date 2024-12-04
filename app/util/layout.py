import streamlit as st
from st_pages import show_pages, Page


def output_layout():
    show_pages (
        [
            Page(
                "./app.py", 
                "Home",
                ":🏠:",
                use_relative_hash=True,
                ),

            Page(
                "./pages/analise.py",
                "Análise e Insights",
                ":chart_with_upwards_trend:",
                use_relative_hash=True,
            ),

            Page(
                "./pages/dashboard.py",
                "Dashboard",
                "💻",
                use_relative_hash=True,
            ),

            Page(
                "./pages/conclusao.py",
                "Conclusão",
                ":white_check_mark:",
                use_relative_hash=True,
            ),

            Page(
                "./pages/referencias.py",
                "Referências",
                "📖",
                use_relative_hash=True,
            )
        ]
    )