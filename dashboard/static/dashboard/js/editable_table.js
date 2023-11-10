// editable_table.js
$(document).ready(function() {
        $('.save-btn').on('click', function() {
        var row = $(this).closest('tr');
        var id = row.find('input[name="id"]').val();

        var data = {
            'Name': row.find('td:nth-child(2)').text(),
            'Age': row.find('td:nth-child(3)').text(),
            'Stage': row.find('td:nth-child(4)').text(),
            'Description': row.find('td:nth-child(5)').text(),
            'Sequencer': row.find('td:nth-child(6)').text(),
            'Gene': row.find('td:nth-child(7)').text(),
            'cDNA_variant': row.find('td:nth-child(8)').text(),
            'protein_variant': row.find('td:nth-child(9)').text(),
            'genomic_variant': row.find('td:nth-child(10)').text(),
            'Classification': row.find('td:nth-child(11)').text(),
        };

        $.ajax({
            type: 'POST',
            url: '/editvariant/' + id,
            data: data,
            headers: {
                'X-CSRFToken': document.cookie.match(/csrftoken=([^ ;]+)/)[1],
            },
            success: function(response) {
                Swal.fire({
                    icon: 'success',
                    title: 'Data updated successfully!',
                });
            },
            error: function(error) {
                console.log(error);
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'Something went wrong!',
                });
            }
        });
    });
});