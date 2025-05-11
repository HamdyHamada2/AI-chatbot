using System.ComponentModel.DataAnnotations;

namespace AIChatBot.Models
{
    public class Product
    {
        [Key]
        public int Id { get; set; }

        [Required]
        public string Name { get; set; }

        public string Type { get; set; }

        public string Description { get; set; }

        public string Usage { get; set; }

        public string Installation { get; set; }
    }
}