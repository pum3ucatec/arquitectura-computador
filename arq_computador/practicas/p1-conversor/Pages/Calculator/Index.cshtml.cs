using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using p1_conversor.Models; // Asegúrate de usar tu namespace correcto

namespace p1_conversor.Pages.Calculator
{
    public class IndexModel : PageModel
    {
        [BindProperty]
        public BaseConverter Input { get; set; } = new BaseConverter();

        public string Result { get; set; }

        public void OnGet()
        {
            // Inicialización opcional
        }

        public IActionResult OnPost()
        {
            if (ModelState.IsValid)
            {
                Result = Input.Convert();
            }
            return Page();
        }
    }
}
