import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.InetAddress;

public class NetworkDiagnostics {
    private final String os = System.getProperty("os.name").toLowerCase();

    public String traceRoute(InetAddress address) {
        String route = "";
        try {
            Process traceRt;
            if (os.contains("win")) {
                traceRt = Runtime.getRuntime().exec("tracert " + address.getHostAddress());
            } else {
                traceRt = Runtime.getRuntime().exec("traceroute " + address.getHostAddress());
            }

            BufferedReader reader = new BufferedReader(new InputStreamReader(traceRt.getInputStream()));
            String line;
            while ((line = reader.readLine()) != null) {
                route += line + "\n";
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return route;
    }

    public static void main(String[] args) {
        try {
            InetAddress targetAddress = InetAddress.getByName("www.google.com");
            NetworkDiagnostics networkDiagnostics = new NetworkDiagnostics();
            String traceResult = networkDiagnostics.traceRoute(targetAddress);
            System.out.println("Traceroute result:\n" + traceResult);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
