$(function () {
  var loadForm = function () {
    console.log("Load Form Run");
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-CRUD").modal("show");
      },
      success: function (data) {
        console.log(data.html_form);
        $("#modal-CRUD").find(".modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    console.log("Save form run");
    var form = $(this);
    console.log("'#" + form.attr("table-id") + "'");
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          console.log("Data is valid");
          // $(".js-update-table").find("tbody").html(data.html_reading_list);
            console.log("RL=", data.html_reading_list);
          $("#" + form.attr("table-id")).find("tbody").html(data.html_reading_list);
          $("#modal-CRUD").modal("hide");
        }
        else {
          console.log("Data form is not Valid");
          $("#modal-CRUD").find(".modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };

  /* Binding */

  // Create Person
  $(".js-create-person").click(loadForm);
  $("#modal-CRUD").on("submit", ".js-person-create-form", saveForm);

  // Update Person
  $("#people-table").on("click", ".js-update-person", loadForm);
  $("#modal-CRUD").on("submit", ".js-person-update-form", saveForm);

  // Delete person
  $("#people-table").on("click", ".js-delete-person", loadForm);
  $("#modal-CRUD").on("submit", ".js-person-delete-form", saveForm);

  //Create Wedding
  $(".js-create-wedding").click(loadForm);
  $("#modal-CRUD").on("submit", ".js-wedding-create-form", saveForm);

  // Update Wedding
  $("#wedding-table").on("click", ".js-update-wedding", loadForm);
  $("#wedding-update-form").on("submit", ".js-wedding-update-form", saveForm);

  // Delete Wedding
  $("#wedding-table").on("click", ".js-delete-wedding", loadForm);
  $("#modal-CRUD").on("submit", ".js-wedding-delete-form", saveForm);

  // Create Reading
  $(".js-create-reading").click(loadForm);
  $("#modal-CRUD").on("submit", ".js-reading-create-form", saveForm);

  // Update Reading
  $("#readings-table").on("click", ".js-update-reading", loadForm);
  $("#modal-CRUD").on("submit", ".js-reading-update-form", saveForm);

  // Delete Reading
  $("#readings-table").on("click", ".js-delete-reading", loadForm);
  $("#modal-CRUD").on("submit", ".js-reading-delete-form", saveForm);

  // Create Hymn
  $(".js-create-hymn").click(loadForm);
  $("#modal-CRUD").on("submit", ".js-hymn-create-form", saveForm);

  // Update Hymn
  $("#hymns-table").on("click", ".js-update-hymn", loadForm);
  $("#modal-CRUD").on("submit", ".js-hymn-update-form", saveForm);

  // Delete Reading
  $("#hymns-table").on("click", ".js-delete-hymn", loadForm);
  $("#modal-CRUD").on("submit", ".js-hymn-delete-form", saveForm);


  // $(".js-create-person").click(function () {
  //   var btn = $(this);
  //   $.ajax({
  //     url: btn.attr("data-url"),
  //     type: 'get',
  //     dataType: 'json',
  //     beforeSend: function () {
  //       $("#modal-person").modal("show");
  //     },
  //     success: function (data) {
  //       $("#modal-person .modal-content").html(data.html_form);
  //     }
  //   });
  // });

  // $("#modal-person").on("submit", ".js-person-create-form", function () {
  //     console.log("Modal Person Submitted");
  //   var form = $(this);
  //   $.ajax({
  //     url: form.attr("action"),
  //     data: form.serialize(),
  //     type: form.attr("method"),
  //     dataType: 'json',
  //     success: function (data) {
  //       if (data.form_is_valid) {
  //           $("#people-table tbody").html(data.html_people_list);
  //           $("#modal-person").modal("hide");
  //       }
  //       else {
  //         $("#modal-person .modal-content").html(data.html_form);
  //       }
  //     }
  //   });
  //   return false;
  // });

});

