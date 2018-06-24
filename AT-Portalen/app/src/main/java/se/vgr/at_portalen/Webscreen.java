package se.vgr.at_portalen;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.webkit.WebView;
import android.webkit.WebViewClient;

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

