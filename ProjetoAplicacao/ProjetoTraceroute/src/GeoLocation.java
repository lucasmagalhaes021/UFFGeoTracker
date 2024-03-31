import com.google.gson.Gson;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URL;
import java.net.URLConnection;

public class GeoLocation {
    public static void main(String[] args) {
        String ipAddress = "45.6.52.32"; // IP address to query

        try {
            // Make the GET request to the API
            String apiUrl = "http://ip-api.com/json/" + ipAddress;
            URL url = new URL(apiUrl);
            URLConnection connection = url.openConnection();
            connection.connect();

            // Read the response
            BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            StringBuilder response = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                response.append(line);
            }
            reader.close();

            // Parse the JSON using Gson
            Gson gson = new Gson();
            IpApiResponse ipApiResponse = gson.fromJson(response.toString(), IpApiResponse.class);

            // Handle the data as needed (e.g., print specific fields)
            System.out.println("IP latitude: " + ipApiResponse.lat);
            System.out.println("IP longitude: " + ipApiResponse.lon);
            System.out.println("Country: " + ipApiResponse.country);
            System.out.println("City: " + ipApiResponse.city);
            // ... other fields you want to extract

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

// Define a class to map the JSON response
class IpApiResponse {
    String query;
    String country;
    String city;
    String lat;
    String lon;
    // ... other fields you want to extract
}
