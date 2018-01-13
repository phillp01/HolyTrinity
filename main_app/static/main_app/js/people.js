$(function () {

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-CRUD").modal("show");
      },
      success: function (data) {
        $("#modal-CRUD").find(".modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $(".js-update-table").find("tbody").html(data.html_list);
          $("#modal-CRUD").modal("hide");
        }
        else {
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
  $("#modal-CRUD").on("submit", ".js-wedding-update-form", saveForm);

  // Delete Wedding
  $("#wedding-table").on("click", ".js-delete-wedding", loadForm);
  $("#modal-CRUD").on("submit", ".js-wedding-delete-form", saveForm);

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

