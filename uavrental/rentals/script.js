// Sayfa yüklendiğinde UAV listesini almak için AJAX isteği gönder
$(document).ready(function() {
    $.ajax({
        url: '/api/uavs/', // API endpointi
        type: 'GET',
        success: function(response) {
            // Başarılı bir şekilde veri alındığında burası çalışır
            displayUAVs(response); // UAV listesini gösteren fonksiyonu çağır
        },
        error: function(xhr, status, error) {
            // Hata durumunda burası çalışır
            console.error('Error:', error); // Hata mesajını konsola yazdır
        }
    });
});

// UAV listesini gösteren fonksiyon
function displayUAVs(uavs) {
    var uavList = document.getElementById('uavList'); // UAV listesi için div öğesini seç
    uavList.innerHTML = ''; // Önceki içeriği temizle

    // Her UAV için bir liste öğesi oluştur
    uavs.forEach(function(uav) {
        var listItem = document.createElement('div');
        listItem.className = 'card mb-3';
        listItem.innerHTML = '<div class="card-body"><h5 class="card-title">' + uav.brand + ' ' + uav.model + '</h5><p class="card-text">Weight: ' + uav.weight + 'kg</p><p class="card-text">Category: ' + uav.category + '</p></div>';
        uavList.appendChild(listItem); // Liste öğesini UAV listesine ekle
    });
}
