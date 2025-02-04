#!/usr/bin/env python3
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def create_playground_dashboard(df):
    # Define colors for each asset type with brighter colors for dark theme
    asset_colors = {
        asset: color for asset, color in zip(
            df['Asset'].unique(),
            [
                '#00b4d8',  # bright blue
                '#ffd60a',  # bright yellow
                '#72efdd',  # turquoise
                '#ff6b6b',  # coral
                '#c77dff',  # bright purple
                '#ff9e00',  # orange
                '#ff0075',  # pink
                '#00f5d4',  # cyan
                '#fee440',  # yellow
                '#7209b7'   # purple
            ]
        )
    }
    
    fig = make_subplots(
        rows=3, cols=2,
        subplot_titles=(
            'Aantal per Type',
            'Inspectiekosten Verdeling',
            'Storingskosten vs Levensduur',
            'Periodiek Onderhoudskosten',
            'Groot Onderhoud Prognose',
            'Exploitatiebudget Analyse'
        ),
        specs=[[{"type": "bar"}, {"type": "pie"}],
               [{"type": "scatter"}, {"type": "bar"}],
               [{"type": "scatter"}, {"type": "bar"}]]
    )

    # Aantal per type
    fig.add_trace(go.Bar(
        x=df['Asset'],
        y=df['Aantal'],
        name='Aantal per Type',
        marker_color=[asset_colors[asset] for asset in df['Asset']]
    ), row=1, col=1)

    # Inspectiekosten verdeling
    fig.add_trace(go.Pie(
        labels=df['Asset'],
        values=df['Inspectie kosten'],
        name='Inspectiekosten',
        marker=dict(colors=[asset_colors[asset] for asset in df['Asset']])
    ), row=1, col=2)

    # Storingskosten vs levensduur
    for asset in df['Asset'].unique():
        asset_data = df[df['Asset'] == asset]
        fig.add_trace(go.Scatter(
            x=asset_data['Rest-levensduur (jr)'],
            y=asset_data['Storingskosten'],
            mode='markers+text',
            text=asset_data['Asset'],
            marker=dict(
                size=15,
                color=asset_colors[asset],
                line=dict(color='#1f1f1f', width=1)
            ),
            name=asset
        ), row=2, col=1)

    # Periodieke kosten
    fig.add_trace(go.Bar(
        x=df['Asset'],
        y=df['Periodieke kosten'],
        name='Periodieke Kosten',
        marker_color=[asset_colors[asset] for asset in df['Asset']]
    ), row=2, col=2)

    # Groot onderhoud prognose
    for asset in df['Asset'].unique():
        asset_data = df[df['Asset'] == asset]
        fig.add_trace(go.Scatter(
            x=asset_data['Rest-levensduur (jr)'],
            y=asset_data['Groot onderhoud'],
            mode='lines+markers',
            name=asset,
            line=dict(color=asset_colors[asset]),
            marker=dict(color=asset_colors[asset])
        ), row=3, col=1)

    # Exploitatiebudget
    fig.add_trace(go.Bar(
        x=df['Asset'],
        y=df['Globale Exploitatiebudget'],
        name='Exploitatiebudget',
        marker_color=[asset_colors[asset] for asset in df['Asset']]
    ), row=3, col=2)

    # Update layout with dark theme
    fig.update_layout(
        height=1500,
        title_text='Speelvoorzieningen Kosten Analyse',
        showlegend=True,
        template="plotly_dark",
        paper_bgcolor='#1f1f1f',
        plot_bgcolor='#1f1f1f',
        font=dict(
            family="Arial",
            size=12,
            color='white'
        ),
    )
    
    # Update axes labels and styling
    for i in range(1, 4):
        for j in range(1, 3):
            fig.update_xaxes(
                showgrid=True,
                gridwidth=1,
                gridcolor='#2f2f2f',
                row=i,
                col=j,
                color='white'
            )
            fig.update_yaxes(
                showgrid=True,
                gridwidth=1,
                gridcolor='#2f2f2f',
                row=i,
                col=j,
                color='white'
            )
    
    # Update specific axis labels
    fig.update_xaxes(title_text="Asset Type", row=1, col=1)
    fig.update_xaxes(title_text="Restlevensduur (jaren)", row=2, col=1)
    fig.update_xaxes(title_text="Asset Type", row=2, col=2)
    fig.update_xaxes(title_text="Restlevensduur (jaren)", row=3, col=1)
    fig.update_xaxes(title_text="Asset Type", row=3, col=2)
    
    fig.update_yaxes(title_text="Aantal", row=1, col=1)
    fig.update_yaxes(title_text="Storingskosten (€)", row=2, col=1)
    fig.update_yaxes(title_text="Periodieke Kosten (€)", row=2, col=2)
    fig.update_yaxes(title_text="Groot Onderhoud (€)", row=3, col=1)
    fig.update_yaxes(title_text="Budget (€)", row=3, col=2)
    
    return fig

if __name__ == '__main__':
    # Read the playground costs data
    print("Reading playground costs data...")
    df = pd.read_csv('playground_costs.csv')
    
    # Create and show the dashboard
    print("Creating visualization dashboard...")
    fig = create_playground_dashboard(df)
    fig.show()
    print("Done! The visualization should open in your browser.")
