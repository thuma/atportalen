package se.vgr.at_portalen;

import android.app.DownloadManager;
import android.net.Uri;
import android.os.Environment;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.webkit.CookieManager;
import android.webkit.DownloadListener;
import android.webkit.URLUtil;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Toast;

public class Webscreen extends AppCompatActivity {
    WebView webView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_webscreen);
        webView = (WebView) findViewById(R.id.webwindow);
        webView.getSettings().setJavaScriptEnabled(true);

        webView.setWebViewClient(new WebViewClient() {

            @Override
            public void onPageFinished(WebView view, String url) {
                // do your javascript injection here, remember "javascript:" is needed to recognize this code is javascript
                webView.loadUrl(
                        "javascript:css = '#tblMid { width:100%;} #tblMain { margin-top:0px !important;} #tblMain img { width:0px;height:0px} #mdMid { padding:0px !important; } #tblMid2 { width:100% !important; } table.mid { width: 100% !important; }';" +
                                "css = css + '#TopMenu {display:none;} #header {display:none;} #leftcol {display:block !important; float:none !important;} #rightcol {display:block !important; float:none !important;} #PageContentInner {margin: 0px !important;} #page { padding:0px !important; margin:0px !importnat;min-width: 0 !important;} div.FooterWrapper, #footerInner { min-width: 0px !important} #centercol {width: 96% !important; margin:0px !important} .RightblockEditorContent { position: inherit !important; }'; " +
                                "head = document.head; style = document.createElement('style'); style.type = 'text/css'; style.appendChild(document.createTextNode(css)); head.appendChild(style);"
                );
             }
        });

        webView.setDownloadListener(new DownloadListener() {

            @Override
            public void onDownloadStart(String url, String userAgent,
                                        String contentDisposition, String mimetype,
                                        long contentLength) {
                DownloadManager.Request request = new DownloadManager.Request(
                        Uri.parse(url));
                final String filename = URLUtil.guessFileName(url, contentDisposition, mimetype);

                String cookies = CookieManager.getInstance().getCookie(url);
                request.addRequestHeader("cookie", cookies);
                request.addRequestHeader("User-Agent", userAgent);
                request.allowScanningByMediaScanner();
                request.setNotificationVisibility(DownloadManager.Request.VISIBILITY_VISIBLE_NOTIFY_COMPLETED); //Notify client once download is completed!
                request.setDestinationInExternalPublicDir(Environment.DIRECTORY_DOWNLOADS, filename);
                DownloadManager dm = (DownloadManager) getSystemService(DOWNLOAD_SERVICE);
                dm.enqueue(request);
                Toast.makeText(getApplicationContext(), "Hämtar fil", //To notify the Client that the file is being downloaded
                        Toast.LENGTH_LONG).show();
            }
        });

        webView.loadUrl("https://epiintra.vgregion.se/su/at");

    }
    @Override
    public void onBackPressed() {
        if (webView.canGoBack()) {
            webView.goBack();
            return;
        } else {
            super.onBackPressed();
        }
    }
}

