from typing import List
import matplotlib.pyplot as plt

async def generate_score_report(data: List[dict]):
    names = [item['name'] for item in data]
    pre_test_scores = [item['Pre Test'] for item in data]
    post_test_scores = [item['Post Test'] for item in data]
    
    print(pre_test_scores)
    print(post_test_scores)

    # Generate double bar graph
    plt.figure(figsize=(25, 15))
    plt.bar(names, pre_test_scores, color='b', width=0.6, align='center', label='Pre Test')
    plt.bar(names, post_test_scores, color='g', width=0.6, align='edge', label='Post Test')
    plt.xlabel('Name')
    plt.ylabel('Score')
    plt.title('Pre Test vs Post Test Scores')
    plt.legend()

    # Save the plot to a file
    double_bar_filename = "scores.png"
    plt.savefig(double_bar_filename)
    plt.close()
    return double_bar_filename
    
    
async def generate_pie_chart(data: List[dict]):
    names = [item['name'] for item in data]
    scores = [item['value'] for item in data]
    
    plt.figure(figsize=(6, 6))
    plt.pie(scores, labels=names, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.title("Satisfaction Index")
    # Convert the chart to bytes
    pie_filename = "satisfaction.png"
    plt.savefig(pie_filename)
    plt.close()
    return pie_filename