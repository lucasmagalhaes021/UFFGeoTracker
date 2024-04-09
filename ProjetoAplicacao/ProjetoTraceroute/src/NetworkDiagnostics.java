import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.InetAddress;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class NetworkDiagnostics {
    private final String os = System.getProperty("os.name").toLowerCase();

    public String traceRoute(InetAddress address) {
        StringBuilder route = new StringBuilder();
        try {
            Process traceRt;
            if (os.contains("win")) {
                traceRt = Runtime.getRuntime().exec("tracert " + address.getHostAddress());
            } else {
                traceRt = Runtime.getRuntime().exec("traceroute " + address.getHostAddress());
            }

            BufferedReader reader = new BufferedReader(new InputStreamReader(traceRt.getInputStream()));
            String line;
            boolean firstLine = true; // To skip the first line (repeated last hop)
            while ((line = reader.readLine()) != null) {
                if (firstLine) {
                    firstLine = false;
                    continue;
                }
                // Extract IP address using regular expression
                //String ipAddress = extractIpAddress(line);
                String ipAddress = line;
                if (ipAddress != null) {
                    route.append(ipAddress).append("\n");
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return route.toString();
    }

    private String extractIpAddress(String line) {
        // Regular expression to match IPv4 addresses
        String regex = "\\b(?:\\d{1,3}\\.){3}\\d{1,3}\\b";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(line);
        if (matcher.find()) {
            return matcher.group();
        }
        return null;
    }

    public static void main(String[] args) {
        try {
            InetAddress targetAddress = InetAddress.getByName("salateorica.com.br");
            NetworkDiagnostics networkDiagnostics = new NetworkDiagnostics();
            String traceResult = networkDiagnostics.traceRoute(targetAddress);
            System.out.println("Traceroute result (IP addresses only):\n" + traceResult);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
