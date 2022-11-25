@Entity
public class Coffee extends Product {

  @NotBlank(message = "Flavor is required")
  public String flavor;

  public String flavorNotes;

  @NotBlank(message = "Description is required")
  public String description;

  @NotBlank(message = "Location is required")
  public String location;

  @NotBlank(message = "Roaster is required")
  public String roaster;

  @NotBlank(message = "ImageURL is required")
  public String imgURL;

  @NotBlank(message = "Roast-level is required")
  public int roastLevel;

  public String roasterNotes;
}
