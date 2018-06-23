package se.vgr.tp_portal_reader;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.webkit.WebView;
import android.webkit.WebViewClient;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        final WebView webView = (WebView)findViewById(R.id.webbsida);
        webView.getSettings().setJavaScriptEnabled(true);
        webView.setWebViewClient(new WebViewClient() {

            @Override
            public void onPageFinished(WebView view, String url) {
                // do your javascript injection here, remember "javascript:" is needed to recognize this code is javascript
                webView.loadUrl(
                        "javascript:css = '#tblMid { width:100%;} #tblMain { margin-top:0px !important;} #tblMain img { width:0px;height:0px} #mdMid { padding:0px !important; } #tblMid2 { width:100% !important; } table.mid { width: 100% !important; }';"+
                                "css = css + '#TopMenu {display:none;}'" +
                        "head = document.head; style = document.createElement('style'); style.type = 'text/css'; style.appendChild(document.createTextNode(css)); head.appendChild(style);"
                 );
            }
        });
        webView.loadUrl("https://epiintra.vgregion.se/su/at");
    }
}