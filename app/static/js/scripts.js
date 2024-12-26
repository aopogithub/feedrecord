document.addEventListener('DOMContentLoaded', function() {
    const ctx = document.getElementById('feedingChart').getContext('2d');
    const feedingData = {
        labels: [], // 喂养记录的日期或时间
        datasets: [{
            label: '亲喂',
            data: [], // 亲喂记录的数据
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
        }, {
            label: '瓶喂',
            data: [], // 瓶喂记录的数据
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1
        }]
    };

    // 从后端获取喂养记录数据
    fetch('/api/feeding_records')
        .then(response => response.json())
        .then(data => {
            data.forEach(record => {
                feedingData.labels.push(record.date);
                feedingData.datasets[0].data.push(record.breastfeeding);
                feedingData.datasets[1].data.push(record.bottlefeeding);
            });

            const feedingChart = new Chart(ctx, {
                type: 'line',
                data: feedingData,
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        });

    // 删除记录的确认
    const deleteButtons = document.querySelectorAll('.delete-button');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function() {
            const recordId = this.dataset.recordId;
            if (confirm('确定要删除这条记录吗？')) {
                fetch(`/api/delete_record/${recordId}`, {
                    method: 'DELETE'
                }).then(response => {
                    if (response.ok) {
                        location.reload(); // 刷新页面以更新记录
                    } else {
                        alert('删除记录失败，请重试。');
                    }
                });
            }
        });
    });
});