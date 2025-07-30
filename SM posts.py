import React, { useState } from 'react';
import { Copy, Share2, Users, MessageCircle, Linkedin, Twitter, CheckCircle } from 'lucide-react';

const SocialMediaPostGenerator = () => {
  const [eventInput, setEventInput] = useState('');
  const [selectedTones, setSelectedTones] = useState(['professional']);
  const [generatedPosts, setGeneratedPosts] = useState({});
  const [isGenerating, setIsGenerating] = useState(false);
  const [copiedText, setCopiedText] = useState('');

  const tones = [
    { id: 'professional', name: 'Professional', color: 'bg-blue-100 text-blue-800' },
    { id: 'sarcastic', name: 'Sarcastic', color: 'bg-orange-100 text-orange-800' },
    { id: 'enthusiastic', name: 'Enthusiastic', color: 'bg-green-100 text-green-800' },
    { id: 'casual', name: 'Casual', color: 'bg-purple-100 text-purple-800' },
    { id: 'educational', name: 'Educational', color: 'bg-indigo-100 text-indigo-800' }
  ];

  const platforms = [
    { id: 'linkedin', name: 'LinkedIn', icon: Linkedin, limit: 3000, color: 'text-blue-600' },
    { id: 'twitter', name: 'Twitter', icon: Twitter, limit: 280, color: 'text-sky-500' },
    { id: 'whatsapp', name: 'WhatsApp', icon: MessageCircle, limit: 4096, color: 'text-green-600' }
  ];

  const postTemplates = {
    professional: {
      linkedin: (event) => `🎯 Exciting Development in Gauge Management

We're thrilled to announce: ${event}

At [Company Name], we continue to drive innovation in precision measurement and industrial monitoring solutions. This milestone represents our commitment to delivering cutting-edge SAAS solutions that empower businesses to achieve operational excellence.

Key benefits for our clients:
• Enhanced measurement accuracy
• Streamlined workflow integration  
• Real-time monitoring capabilities
• Scalable enterprise solutions

Ready to transform your gauge management processes? Let's connect and discuss how this advancement can benefit your operations.

#GaugeManagement #SAAS #IndustrialTech #Innovation #PrecisionMeasurement`,

      twitter: (event) => `🚀 Big news in gauge management! ${event}

Our SAAS solution continues to set industry standards for precision measurement and monitoring.

#GaugeManagement #SAAS #IndustrialTech #Innovation`,

      whatsapp: (event) => `🎉 *Exciting Update from [Company Name]*

Hi there! We wanted to share some fantastic news with you:

${event}

This development strengthens our position as a leading SAAS gauge management solution provider. We're committed to helping businesses like yours achieve greater efficiency and accuracy in measurement processes.

Would you like to learn more about how this benefits your operations? We'd love to schedule a brief call to discuss the possibilities.

Best regards,
[Your Name] - CMO`
    },

    sarcastic: {
      linkedin: (event) => `Oh, just another "revolutionary" development in gauge management... 🙄

Kidding! We're actually genuinely excited about: ${event}

While everyone else is still measuring things with rulers from 1995, we're over here building SAAS solutions that actually work. Revolutionary? Maybe. Necessary? Absolutely.

Because apparently, accurate measurements and streamlined processes are still considered "innovative" in 2025. Who knew? 🤷‍♀️

Ready to join the 21st century of gauge management?

#GaugeManagement #SAAS #WelcomeToTheFuture #StillUsingSpreadsheets`,

      twitter: (event) => `Plot twist: ${event} 

And yes, we're still the only ones who think gauge management should actually... work properly. Wild concept, right? 🤯

#GaugeManagement #SAAS #ModernProblems`,

      whatsapp: (event) => `*Well, this happened...* 😏

${event}

I know, I know - another day, another breakthrough in gauge management. Because apparently we're the only ones who think measuring things accurately shouldn't be rocket science.

But hey, someone has to drag this industry into the modern era, right? Might as well be us! 

Want to see what "functional software" looks like? Hit me up! 📱`
    },

    enthusiastic: {
      linkedin: (event) => `🎉 WOW! This is HUGE for gauge management! 

${event}

I can barely contain my excitement about what this means for our industry! 🚀 Our SAAS solution is transforming how businesses approach precision measurement, and this milestone proves we're just getting started!

The impact on operational efficiency is going to be INCREDIBLE:
✨ Game-changing accuracy improvements
✨ Lightning-fast implementation
✨ Mind-blowing ROI potential
✨ Future-proof scalability

This is the kind of innovation that keeps me up at night (in the best way possible)! Who else is ready to revolutionize their measurement processes?! 

LET'S GOOO! 🔥

#GaugeManagement #SAAS #GameChanger #Innovation #Excited`,

      twitter: (event) => `🔥 GAME CHANGER ALERT! 🔥

${event}

This is exactly why I LOVE working in gauge management SAAS! The future is NOW! 🚀

Who's ready to transform their measurement game?!

#GaugeManagement #SAAS #Excited #Innovation`,

      whatsapp: (event) => `🎊 *AMAZING NEWS!* 🎊

${event}

I'm literally buzzing with excitement about this! This is exactly the kind of breakthrough that makes me passionate about what we do every single day! 

Our gauge management SAAS solution is changing the game, and I couldn't be prouder to be part of this journey! The possibilities are ENDLESS! 

Want to experience this excitement firsthand? Let's chat about how this can supercharge your operations! 

*Ready to be amazed?* ⚡️`
    },

    casual: {
      linkedin: (event) => `Hey everyone! 👋

So this cool thing happened: ${event}

Honestly, working in gauge management might not sound like the most exciting field, but moments like these remind me why I love what we do. Our SAAS solution is making real differences for real businesses, and that's pretty awesome.

If you're dealing with measurement headaches or just curious about modern gauge management solutions, feel free to reach out. Always happy to chat about how we can make your processes smoother.

Cheers! 🍻

#GaugeManagement #SAAS #RealTalk`,

      twitter: (event) => `Just happened: ${event}

Pretty cool stuff in the gauge management world! Our SAAS solution keeps getting better 📈

DM me if you want to chat about it! 

#GaugeManagement #SAAS`,

      whatsapp: (event) => `Hey! Hope you're doing well! 

Quick update from our end: ${event}

I thought you might find this interesting since you're always looking for ways to improve your measurement processes. Our SAAS solution has been helping a lot of companies streamline their operations.

No pressure, but if you ever want to chat about how this might work for you, just give me a shout! 

Have a great day! 😊`
    },

    educational: {
      linkedin: (event) => `📚 Industry Insight: Understanding Gauge Management Evolution

Today's milestone: ${event}

Let's break down what this means for modern manufacturing and quality control:

🔍 **The Challenge**: Traditional gauge management often relies on manual processes, leading to inconsistencies and inefficiencies.

💡 **The Solution**: SAAS-based gauge management systems provide:
• Centralized data management
• Automated calibration tracking  
• Real-time compliance monitoring
• Predictive maintenance insights

📊 **Industry Impact**: Companies implementing digital gauge management see average improvements of:
- 35% reduction in measurement errors
- 50% faster compliance reporting
- 25% decrease in equipment downtime

🎯 **Key Takeaway**: The shift to cloud-based gauge management isn't just about technology—it's about building sustainable, scalable quality systems.

What aspects of gauge management digitization are you most curious about?

#GaugeManagement #QualityControl #Manufacturing #SAAS #DigitalTransformation`,

      twitter: (event) => `📖 Quick lesson: ${event}

Why SAAS gauge management matters:
✅ Centralized tracking
✅ Automated compliance  
✅ Predictive insights
✅ Scalable solutions

The future of precision measurement is digital! 

#GaugeManagement #Education #SAAS`,

      whatsapp: (event) => `📚 *Educational Moment!*

${event}

Since you're interested in operational improvements, here's why this matters:

*Traditional gauge management challenges:*
- Manual tracking and errors
- Compliance headaches  
- Equipment downtime surprises

*Modern SAAS solutions offer:*
- Automated processes
- Real-time insights
- Predictive maintenance
- Seamless compliance

The result? Companies typically see 35% fewer measurement errors and 50% faster reporting.

Want to dive deeper into how this could transform your operations? Let's schedule a brief educational call!`
    }
  };

  const handleToneToggle = (toneId) => {
    setSelectedTones(prev => 
      prev.includes(toneId) 
        ? prev.filter(id => id !== toneId)
        : [...prev, toneId]
    );
  };

  const generatePosts = () => {
    if (!eventInput.trim()) return;
    
    setIsGenerating(true);
    
    // Simulate API call delay
    setTimeout(() => {
      const posts = {};
      
      selectedTones.forEach(tone => {
        posts[tone] = {};
        platforms.forEach(platform => {
          if (postTemplates[tone] && postTemplates[tone][platform.id]) {
            posts[tone][platform.id] = postTemplates[tone][platform.id](eventInput);
          }
        });
      });
      
      setGeneratedPosts(posts);
      setIsGenerating(false);
    }, 1500);
  };

  const copyToClipboard = async (text, identifier) => {
    try {
      await navigator.clipboard.writeText(text);
      setCopiedText(identifier);
      setTimeout(() => setCopiedText(''), 2000);
    } catch (err) {
      console.error('Failed to copy text: ', err);
      // Fallback for browsers that don't support clipboard API
      const textArea = document.createElement('textarea');
      textArea.value = text;
      document.body.appendChild(textArea);
      textArea.select();
      document.execCommand('copy');
      document.body.removeChild(textArea);
      setCopiedText(identifier);
      setTimeout(() => setCopiedText(''), 2000);
    }
  };

  const getCharacterCount = (text, limit) => {
    const count = text.length;
    const isOverLimit = count > limit;
    const isNearLimit = count > limit * 0.9;
    
    let colorClass = 'text-gray-500';
    if (isOverLimit) {
      colorClass = 'text-red-500';
    } else if (isNearLimit) {
      colorClass = 'text-yellow-500';
    } else {
      colorClass = 'text-green-500';
    }
    
    return (
      <span className={`text-sm font-medium ${colorClass}`}>
        {count}/{limit} characters {isOverLimit && '(Over limit!)'}
      </span>
    );
  };

  return (
    <div className="max-w-6xl mx-auto p-6 bg-gradient-to-br from-gray-50 to-blue-50 min-h-screen">
      <div className="bg-white rounded-xl shadow-lg p-8">
        <div className="mb-8 text-center">
          <h1 className="text-4xl font-bold text-gray-800 mb-2">Social Media Post Generator</h1>
          <p className="text-lg text-gray-600">SAAS Gauge Management Solution - CMO Content Creator</p>
        </div>

        {/* Event Input Section */}
        <div className="mb-8">
          <label className="block text-lg font-semibold text-gray-700 mb-3">
            Event Description
          </label>
          <textarea
            value={eventInput}
            onChange={(e) => setEventInput(e.target.value)}
            placeholder="Enter your event details here (e.g., 'We just launched our new AI-powered calibration feature that reduces setup time by 60%')"
            className="w-full p-4 border-2 border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 resize-none transition-colors"
            rows="4"
          />
        </div>

        {/* Tone Selection */}
        <div className="mb-8">
          <label className="block text-lg font-semibold text-gray-700 mb-3">
            Select Tones (Multiple Selection Allowed)
          </label>
          <div className="flex flex-wrap gap-3">
            {tones.map(tone => (
              <button
                key={tone.id}
                onClick={() => handleToneToggle(tone.id)}
                className={`px-4 py-2 rounded-full border-2 transition-all duration-200 transform hover:scale-105 ${
                  selectedTones.includes(tone.id)
                    ? `${tone.color} border-current shadow-md`
                    : 'bg-gray-100 text-gray-600 border-gray-300 hover:bg-gray-200'
                }`}
              >
                {tone.name}
              </button>
            ))}
          </div>
          <p className="text-sm text-gray-500 mt-2">
            Selected: {selectedTones.length} tone{selectedTones.length !== 1 ? 's' : ''}
          </p>
        </div>

        {/* Generate Button */}
        <div className="mb-8 text-center">
          <button
            onClick={generatePosts}
            disabled={!eventInput.trim() || selectedTones.length === 0 || isGenerating}
            className="bg-gradient-to-r from-blue-600 to-indigo-600 text-white px-8 py-3 rounded-lg font-semibold hover:from-blue-700 hover:to-indigo-700 disabled:from-gray-300 disabled:to-gray-400 disabled:cursor-not-allowed transition-all duration-200 flex items-center gap-2 mx-auto transform hover:scale-105"
          >
            <Share2 size={20} />
            {isGenerating ? 'Generating Posts...' : 'Generate Posts'}
          </button>
        </div>

        {/* Generated Posts */}
        {Object.keys(generatedPosts).length > 0 && (
          <div className="space-y-8">
            <h2 className="text-2xl font-bold text-gray-800 text-center">Generated Posts</h2>
            
            {selectedTones.map(tone => (
              <div key={tone} className="bg-gradient-to-r from-gray-50 to-blue-50 rounded-xl p-6 shadow-sm">
                <h3 className="text-xl font-semibold text-gray-700 mb-4 capitalize flex items-center gap-2">
                  <span className="w-3 h-3 bg-blue-500 rounded-full"></span>
                  {tone} Tone
                </h3>
                
                <div className="grid gap-6">
                  {platforms.map(platform => {
                    const PlatformIcon = platform.icon;
                    const post = generatedPosts[tone]?.[platform.id];
                    const copyId = `${tone}-${platform.id}`;
                    
                    if (!post) return null;
                    
                    return (
                      <div key={platform.id} className="bg-white rounded-lg border-2 border-gray-200 p-6 hover:shadow-md transition-shadow">
                        <div className="flex items-center justify-between mb-4">
                          <div className="flex items-center gap-3">
                            <PlatformIcon className={`${platform.color} w-6 h-6`} />
                            <span className="font-semibold text-gray-700 text-lg">
                              {platform.name}
                            </span>
                          </div>
                          <button
                            onClick={() => copyToClipboard(post, copyId)}
                            className="flex items-center gap-2 bg-blue-100 hover:bg-blue-200 text-blue-700 px-4 py-2 rounded-lg transition-colors duration-200"
                          >
                            {copiedText === copyId ? (
                              <>
                                <CheckCircle size={16} />
                                Copied!
                              </>
                            ) : (
                              <>
                                <Copy size={16} />
                                Copy
                              </>
                            )}
                          </button>
                        </div>
                        
                        <div className="mb-3">
                          {getCharacterCount(post, platform.limit)}
                        </div>
                        
                        <div className="bg-gray-50 p-4 rounded-lg border text-sm whitespace-pre-wrap font-mono leading-relaxed">
                          {post}
                        </div>
                      </div>
                    );
                  })}
                </div>
              </div>
            ))}
          </div>
        )}

        {/* Usage Instructions */}
        <div className="mt-12 bg-gradient-to-r from-blue-50 to-indigo-50 rounded-xl p-6 border border-blue-200">
          <h3 className="text-lg font-semibold text-blue-800 mb-3 flex items-center gap-2">
            <Users size={20} />
            How to Use:
          </h3>
          <ol className="list-decimal list-inside space-y-2 text-blue-700">
            <li>Enter your event details in the text area above</li>
            <li>Select one or more tones for your posts (multiple selection allowed)</li>
            <li>Click "Generate Posts" to create content for all platforms</li>
            <li>Review generated posts and copy the ones you want to use</li>
            <li>Customize company name and personal details before posting</li>
            <li>Check character limits before posting on each platform</li>
          </ol>
          
          <div className="mt-4 p-3 bg-blue-100 rounded-lg">
            <p className="text-sm text-blue-800">
              <strong>Pro Tip:</strong> LinkedIn posts can be longer and more detailed, Twitter posts should be concise and punchy, while WhatsApp posts can be more personal and conversational.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default SocialMediaPostGenerator;