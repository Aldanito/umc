(function ($) {
    "use strict";
    
    // Dropdown on mouse hover
    $(document).ready(function () {
        function toggleNavbarMethod() {
            if ($(window).width() > 992) {
                $('.navbar .dropdown').on('mouseover', function () {
                    $('.dropdown-toggle', this).trigger('click');
                }).on('mouseout', function () {
                    $('.dropdown-toggle', this).trigger('click').blur();
                });
            } else {
                $('.navbar .dropdown').off('mouseover').off('mouseout');
            }
        }
        toggleNavbarMethod();
        $(window).resize(toggleNavbarMethod);
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Vendor carousel
    $('.vendor-carousel').owlCarousel({
        loop: true,
        margin: 29,
        nav: false,
        autoplay: true,
        smartSpeed: 1000,
        responsive: {
            0:{
                items:2
            },
            576:{
                items:3
            },
            768:{
                items:4
            },
            992:{
                items:5
            },
            1200:{
                items:6
            }
        }
    });


    // Related carousel
    $('.related-carousel').owlCarousel({
        loop: true,
        margin: 29,
        nav: false,
        autoplay: true,
        smartSpeed: 1000,
        responsive: {
            0:{
                items:1
            },
            576:{
                items:2
            },
            768:{
                items:3
            },
            992:{
                items:4
            }
        }
    });


    // Product Quantity
    $('.quantity button').on('click', function () {
        var button = $(this);
        var oldValue = button.parent().parent().find('input').val();
        if (button.hasClass('btn-plus')) {
            var newVal = parseFloat(oldValue) + 1;
        } else {
            if (oldValue > 0) {
                var newVal = parseFloat(oldValue) - 1;
            } else {
                newVal = 0;
            }
        }
        button.parent().parent().find('input').val(newVal);
    });
    
})(jQuery);
// измененные языки
let langs = ['en', 'ru', 'kz'];
var lang = localStorage.getItem('lang') || 'ru';

setLangStyles(lang);

window.onload = function() {
  localStorage.setItem('lang', lang);
};

function setStyles(styles) {
  var elementId = '__lang_styles';
  var element = document.getElementById(elementId);
  if (element) {
    element.remove();
  }

  let style = document.createElement('style');
  style.id = elementId;
  style.type = 'text/css';

  if (style.styleSheet) {
    style.styleSheet.cssText = styles;
  } else {
    style.appendChild(document.createTextNode(styles));
  }
  document.getElementsByTagName('head')[0].appendChild(style);
}

function setLang(lang) {
  setLangStyles(lang);
  localStorage.setItem('lang', lang); 
}

function setLangStyles(lang) {
  let styles = langs
    .filter(function (l) {
      return l != lang;
    })
    .map(function (l) {
      return ':lang('+ l +') { display: none; }';
    })
    .join(' ');

  setStyles(styles);
}



