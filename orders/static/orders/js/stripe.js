$(function() {

  $ (#user_form).submit(function(){
  var form = this;

  var card = {
    number: $("#credit_card_number").val(),
    expMonth: $("#expiration_month").val(),
    expYear: $("#expiration_year").val(),
    cvc: $("#cvv").val()
  };

  Stripe.createToken(card, function(status, response) {
    if (status === 200) {
      console.log(status, response);
      $("#credit-card-errors").hide();
      $("#id_stripe_id").val(response.id);
      form.submit();

    } else {
      $("#stripe-error-message").text(response.error.message);
      $("#credit-card-errors").show();
      $("#user_submt").attr("disabled", false);
    }
  });

    return false;
  });
});
